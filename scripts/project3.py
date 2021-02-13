#!/usr/bin/env python3
import argparse
import collections
import inspect
import random
import sys
from inspect import getmembers, isfunction

import requests


def assert_equal(lhs, rhs, success_output=True):
    if lhs != rhs:
        print(f"Failed: {lhs} != {rhs}")
        print("  Backtrace")
        for frame in inspect.stack()[1:-2]:
            assert len(frame.code_context) == 1
            context = frame.code_context[0].rstrip()
            print(f"  Line {frame.lineno:4d}: {context}")
    elif success_output:
        sys.stdout.write(".")
        sys.stdout.flush()


def assert_not_equal(lhs, rhs):
    if lhs == rhs:
        print(f"Failed: {lhs} == {rhs}")
        print("  Backtrace")
        for frame in inspect.stack()[1:-2]:
            assert len(frame.code_context) == 1
            context = frame.code_context[0].rstrip()
            print(f"  Line {frame.lineno:4d}: {context}")
    else:
        sys.stdout.write(".")
        sys.stdout.flush()


def connect(
    url,
    callback=None,
    expected_status=200,
    last_event_id=None,
    tokens=None,
    username=None,
):
    if tokens is not None and username is None:
        raise Exception("username must be provided when tokens are provided")

    if tokens is None:
        username, tokens = login(url, username=username)

    headers = {}
    if last_event_id:
        headers["Last-Event-Id"] = last_event_id
    with requests.get(
        f"{url}/stream/{tokens['stream_token']}", headers=headers, stream=True
    ) as response:
        assert_equal(response.status_code, expected_status, success_output=False)
        if callback is not None:
            callback(response=response, tokens=tokens, username=username)


def login(url, *, username=None):
    if username is None:
        username = str(random.randint(0, 9999999))
    response = requests.post(
        f"{url}/login", data={"password": username, "username": username}
    )
    assert_equal(response.status_code, 201, success_output=False)
    return username, response.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")

    subparsers = parser.add_subparsers(dest="command", metavar="command", required=True)
    parser_stream = subparsers.add_parser("stream", help="Connect to stream")
    parser_stream.add_argument("-l", "--last-event-id")
    parser_stream.add_argument("-u", "--user")

    parser_test = subparsers.add_parser("test", help="Run tests")
    arguments = parser.parse_args()

    if arguments.command == "test":
        for name, function in getmembers(sys.modules[__name__], isfunction):
            if not name.startswith("test_"):
                continue
            function(arguments.url)
        return

    assert arguments.command == "stream"

    url = arguments.url

    def callback(response, tokens, username):
        for line in read_stream_lines(response):
            print(repr(line))

    connect(
        url,
        callback=callback,
        last_event_id=arguments.last_event_id,
        username=arguments.user if arguments.user else random.randint(0, 9999999),
    )


def read_stream_lines(response):
    data = ""
    while True:
        read = response.raw.read(2).decode("utf-8")
        if not read:
            assert data == ""
            break
        data += read
        parts = data.split("\n")
        for part in parts[:-1]:
            yield part
        data = parts[-1]


def send_message(url, token, *, expected_status=201, message):
    response = requests.post(
        f"{url}/message",
        data={"message": message},
        headers={"authorization": f"Bearer {token}"},
    )
    assert_equal(response.status_code, expected_status, success_output=False)
    return response.headers.get("token")


def test_login__fails_when_user_already_connected_to_stream(url):
    saved_tokens = None
    saved_username = None

    def callback(response, tokens, username):
        nonlocal saved_tokens
        nonlocal saved_username
        saved_tokens = tokens
        saved_username = username

        login_response = requests.post(
            f"{url}/login", data={"password": username, "username": username}
        )
        assert_equal(login_response.status_code, 409)

        # Ensure original message token still works
        send_message(url, tokens["message_token"], message="/quit")
        # Consume all messages quickly
        collections.deque(read_stream_lines(response), maxlen=0)

    connect(url, callback=callback)

    # Ensure original stream token still works
    connect(url, tokens=saved_tokens, username=saved_username)


def test_login__fails_with_invalid_password(url):
    username, _tokens = login(url)

    response = requests.post(
        f"{url}/login", data={"username": username, "password": "invalid"}
    )
    assert_equal(response.status_code, 403)


def test_login__fails_with_missing_or_blank_fields(url):
    username = str(random.randint(0, 9999999))

    response = requests.post(f"{url}/login")
    assert_equal(response.status_code, 422)

    response = requests.post(f"{url}/login", data={"password": username})
    assert_equal(response.status_code, 422)

    response = requests.post(f"{url}/login", data={"username": username})
    assert_equal(response.status_code, 422)

    response = requests.post(
        f"{url}/login", data={"password": "", "username": username}
    )
    assert_equal(response.status_code, 422)

    response = requests.post(
        f"{url}/login", data={"password": username, "username": ""}
    )
    assert_equal(response.status_code, 422)


def test_login__new_tokens_are_issued_on_subsequent_login(url):
    username, first_tokens = login(url)
    second_username, second_tokens = login(url, username=username)
    assert_equal(username, second_username)

    assert_not_equal(first_tokens["message_token"], second_tokens["message_token"])
    assert_not_equal(first_tokens["stream_token"], second_tokens["stream_token"])

    # Ensure original stream token does not work
    connect(url, expected_status=403, tokens=first_tokens, username=username)

    def callback(response, tokens, username):
        # Ensure original message token does not work
        send_message(
            url,
            first_tokens["message_token"],
            expected_status=403,
            message="new_tokens_are_issued_on_subsequent_login should fail",
        )

        # Ensure new message token works
        send_message(
            url,
            second_tokens["message_token"],
            message="new_tokens_are_issued_on_subsequent_login",
        )

    # Ensure new stream token works
    connect(url, callback=callback, tokens=second_tokens, username=username)


def test_login__new_tokens_are_not_issued_on_failed_subsequent_login(url):
    username, tokens = login(url)
    login_response = requests.post(f"{url}/login", data={})
    assert_equal(login_response.status_code, 422)

    def callback(response, tokens, username):
        send_message(
            url,
            tokens["message_token"],
            message="new_tokens_are_not_issued_on_failed_subsequent_login",
        )

    connect(url, callback=callback, tokens=tokens, username=username)


def test_message__fails_with_missing_or_blank_fields(url):
    token = login(url)[1]["message_token"]

    response = requests.post(
        f"{url}/message", data={"message": "missing authorization header"}
    )
    assert_equal(response.status_code, 403)

    response = requests.post(
        f"{url}/message",
        data={"message": "malformed authorization header"},
        headers={"authorization": f"Bearer: {token}"},
    )
    assert_equal(response.status_code, 403)

    response = requests.post(
        f"{url}/message",
        data={},
        headers={"authorization": f"Bearer {token}"},
    )
    assert_equal(response.status_code, 422)

    send_message(url, token, expected_status=422, message="")


def test_message__fails_when_not_connected_to_stream(url):
    token = login(url)[1]["message_token"]
    send_message(
        url, token, expected_status=409, message="fails_when_not_connected_to_stream"
    )


def test_message__token_can_be_used_only_once(url):
    def callback(response, tokens, username):
        new_token = send_message(
            url, tokens["message_token"], message="Connected to stream"
        )
        send_message(
            url,
            tokens["message_token"],
            expected_status=403,
            message="This message token should no longer be valid",
        )
        send_message(url, new_token, message="Subsequent message using updated token")

    connect(url, callback=callback)


def test_stream__fails_when_already_connected_to_stream(url):
    def callback(response, tokens, username):
        connect(url, expected_status=409, tokens=tokens, username=username)

    connect(url, callback=callback)


def test_stream__fails_with_invalid_token(url):
    response = requests.get(f"{url}/stream/invalidtoken")
    assert_equal(response.status_code, 403)


def test_stream__fails_without_token(url):
    response = requests.get(f"{url}/stream")
    assert_equal(response.status_code, 404)

    response = requests.get(f"{url}/stream/")
    assert_equal(response.status_code, 404)


def test_stream__last_event_id_returns_subset_of_events(url):
    event_ids = []

    def callback(response, tokens, username):
        send_message(url, tokens["message_token"], message="/quit")
        for line in read_stream_lines(response):
            if line.startswith("id: "):
                event_ids.append(line[4:])

    connect(url, callback=callback)

    # Ensure there are no duplicate events
    assert_equal(sorted(event_ids), sorted(set(event_ids)))

    reconnect_event_ids = []

    def callback_expect_new_events(response, tokens, username):
        send_message(url, tokens["message_token"], message="/quit")
        for line in read_stream_lines(response):
            if line.startswith("id: "):
                reconnect_event_ids.append(line[4:])

    connect(url, callback=callback_expect_new_events, last_event_id=event_ids[-1])

    # Ensure there are no duplicate events
    assert_equal(sorted(reconnect_event_ids), sorted(set(reconnect_event_ids)))

    # Ensure there is no overlap
    assert_equal(set(event_ids) & set(reconnect_event_ids), set())


def test_stream__reconnect_closes_connection(url):
    def callback(response, tokens, username):
        send_message(url, tokens["message_token"], message="/reconnect")
        # Consume all messages quickly
        collections.deque(read_stream_lines(response), maxlen=0)

    connect(url, callback=callback)


if __name__ == "__main__":
    sys.exit(main())
