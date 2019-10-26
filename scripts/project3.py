#!/usr/bin/env python3
import argparse
import random
import sys

import requests


def assert_equal(lhs, rhs):
    if lhs != rhs:
        print(f"Failed: {lhs} != {rhs}")


def connect(url, username, last_event_id):
    token = get_token(url, username)
    headers = {}
    if last_event_id:
        headers["Last-Event-Id"] = last_event_id
    with requests.get(
        f"{url}/stream/{token}", headers=headers, stream=True
    ) as response:
        test_message(url, token)

        for line in read_stream_lines(response):
            print(line)


def get_token(url, username):
    response = requests.post(
        f"{url}/login", data={"username": username, "password": username}
    )
    assert_equal(response.status_code, 201)
    return response.json()["token"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--last-event-id")
    parser.add_argument(
        "-F", "--no-failures", action="store_true", help="Skip failure testing"
    )
    parser.add_argument("url")
    arguments = parser.parse_args()

    if not arguments.no_failures:
        test_login__failed(arguments.url)
        test_message__failed(arguments.url)
        test_stream__failed(arguments.url)

    username = random.randint(0, 9999999)
    connect(arguments.url, username, arguments.last_event_id)


def read_stream_lines(response):
    yield "Starting"
    data = ""
    while True:
        data += response.raw.read(2).decode("utf-8")
        parts = data.split("\n")
        for part in parts[:-1]:
            yield part
        data = parts[-1]


def test_login__failed(url):
    username = random.randint(0, 9999999)

    response = requests.post(
        f"{url}/login", data={"username": username, "password": username}
    )
    assert_equal(response.status_code, 201)

    response = requests.post(
        f"{url}/login", data={"username": username, "password": "bad"}
    )
    assert_equal(response.status_code, 403)

    response = requests.post(f"{url}/login", data={"username": "", "password": "bad"})
    assert_equal(response.status_code, 422)

    response = requests.post(
        f"{url}/login", data={"username": username + 1, "password": ""}
    )
    assert_equal(response.status_code, 422)


def test_message(url, token):
    response = requests.post(
        f"{url}/message",
        data={"message": "Hi!"},
        headers={"authorization": f"Bearer {token}"},
    )
    assert_equal(response.status_code, 201)


def test_message__failed(url):
    response = requests.post(
        f"{url}/message",
        data={"message": "this should fail"},
        headers={"authorization": "Bearer invalidtoken"},
    )
    assert_equal(response.status_code, 403)

    token = get_token(url, random.randint(0, 9999999))
    response = requests.post(
        f"{url}/message",
        data={"message": ""},
        headers={"authorization": f"Bearer {token}"},
    )
    assert_equal(response.status_code, 422)


def test_stream__failed(url):
    response = requests.get(f"{url}/stream/invalidtoken")
    assert_equal(response.status_code, 403)


if __name__ == "__main__":
    sys.exit(main())
