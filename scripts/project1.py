#!/usr/bin/env python3
import random
import sys
import time
from urllib.parse import urljoin, urlparse

import jwt
import requests


HTTP_VERBS = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
with open("/usr/share/dict/words") as fp:
    WORDS = fp.read().split()


def count_format(word, number):
    base = f"{number} {word}"
    if number != 1:
        base += "s"
    return base


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} URL")
        return 1

    return score(url=sys.argv[1])


def mix_case(word):
    result = ""
    for character in word:
        if character.isalpha():
            if random.choice([True, False]):
                result += character.upper()
            else:
                result += character.lower()
        else:
            result += character
    return result


def score(url):
    failures = 0

    result = urlparse(url)
    if result.scheme != "https":
        print(f"Scheme is not https: {result.scheme}")
        failures += 1

    if not result.netloc.endswith(".execute-api.us-west-2.amazonaws.com"):
        print(f"Domain does not appear to be lambda: {result.netloc}")
        failures += 1

    if result.path != "/prod/":
        print(f"Resource path must be `/prod/`. Yours: {result.path}")
        failures += 1

    if failures:
        print(count_format("Failure", failures))
        return failures

    failures += test_invalid_urls(url)
    failures += test_invalid_verbs(url, set(HTTP_VERBS) - {"GET"})
    failures += test_invalid_verbs(urljoin(url, "token"), set(HTTP_VERBS) - {"POST"})
    failures += test_token__invalid_content_type(urljoin(url, "token"))
    failures += test_token__invalid_json_body(urljoin(url, "token"))
    failures += test_token__success(urljoin(url, "token"))
    failures += test_root__invalid_header_specification(url)
    failures += test_root__invalid_tokens(url)

    if failures:  # Only run the last tests if everything else passes
        print(count_format("Failure", failures))
        return failures

    failures += test_root__invalid_timeliness(url)
    failures += test_root__success(url)

    if failures == 0:
        print("Passed")
    else:
        print(count_format("Failure", failures))
    return failures


def test_invalid_urls(url):
    """All invalid URLs should return 404, regardless of HTTP verb."""
    failures = 0
    for i in range(10):
        verb = random.choice(HTTP_VERBS)
        path = "/".join([random.choice(WORDS) for _ in range(random.randint(1, 3))])
        test_url = urljoin(url, path)
        response = requests.get(test_url, allow_redirects=False)
        if response.status_code != 404:
            print(
                f"Expected 404 response for `GET {test_url}`. Got {response.status_code}."
            )
            failures += 1
    return failures


def test_invalid_verbs(url, verbs):
    failures = 0
    for verb in sorted(verbs):
        response = requests.request(verb, url, allow_redirects=False)
        if response.status_code != 405:
            print(
                f"Expected 405 response for `{verb} {url}`. Got {response.status_code}."
            )
            failures += 1
    return failures


def test_root__invalid_header_specification(url):
    failures = 0
    for header_value in [None, "", "Bearer: foobar"]:
        response = requests.get(
            url,
            allow_redirects=False,
            headers={mix_case("authorization"): header_value},
        )
        if response.status_code != 403:
            print(f"Expected 403 response for `GET /`. Got {response.status_code}.")
            failures += 1
    return failures


def test_root__invalid_timeliness(url):
    failures = 0
    token = requests.post(
        urljoin(url, "token"),
        allow_redirects=False,
        headers={mix_case("content-type"): "application/json"},
        json={},
    ).json()["token"]

    # Requesting immediately should fail
    response = requests.get(
        url,
        allow_redirects=False,
        headers={mix_case("authorization"): f"Bearer {token}"},
    )
    if response.status_code != 401:
        print(
            f"Expected 401 response for not yet valid token. Got {response.status_code}"
        )
        failures += 1

    print("\t...sleeping 5 seconds")
    time.sleep(5)
    # Requesting after 5 seconds should fail
    response = requests.get(
        url,
        allow_redirects=False,
        headers={mix_case("authorization"): f"Bearer {token}"},
    )
    if response.status_code != 401:
        print(f"Expected 401 response for expired token. Got {response.status_code}")
        failures += 1

    return failures


def test_root__invalid_tokens(url):
    failures = 0
    for security in [(None, "none"), ("NOTASECRET", "HS256")]:
        token = jwt.encode({"data": 1}, *security).decode("utf-8")
        response = requests.get(
            url,
            allow_redirects=False,
            headers={mix_case("authorization"): f"Bearer {token}"},
        )
        if response.status_code != 403:
            print(f"Expected 403 response for `GET /`. Got {response.status_code}.")
            failures += 1
    return failures


def test_root__success(url):
    failures = 0
    for payload in [{}, 1, ["a", 1, "b"], {"user_id": "12345"}]:
        token = requests.post(
            urljoin(url, "token"),
            allow_redirects=False,
            headers={mix_case("content-type"): "application/json"},
            json=payload,
        ).json()["token"]
        print("\t...sleeping 2 seconds")
        time.sleep(2)

        response = requests.get(
            url,
            allow_redirects=False,
            headers={mix_case("authorization"): f"Bearer {token}"},
        )
        if response.status_code != 200:
            print(f"Expected 200 response for `GET /`. Got {response.status_code}.")
            failures += 1
            continue

        if response.headers["Content-Type"] != "application/json":
            # This case _shouldn't_ happen as there's no need to explicitly set the response header.
            print(
                f"Expected Content-Type response header to be `application/json`. Got {response.headers['Content-Type']}."
            )
            failures += 1
            continue

        body = response.json()
        if body != payload:
            print(f"Expected JSON response body to be `{payload}`. Got {body}")
            failures += 1
    return failures


def test_token__invalid_content_type(url):
    failures = 0
    for content_type in [
        "",
        "APPLICATION/JSON",
        "application/x-www-form-urlencoded",
        "multipart/form-data",
        "text/plain",
    ]:
        response = requests.post(
            url,
            allow_redirects=False,
            data="{}",
            headers={"Content-Type": content_type},
        )
        if response.status_code != 415:
            print(
                f"Expected 415 response for /token with content type `{content_type}`. Got {response.status_code}."
            )
            failures += 1
    return failures


def test_token__invalid_json_body(url):
    failures = 0
    for invalid_body in ["", "{", "}", "hello", "{'a': 1}"]:
        response = requests.post(
            url,
            allow_redirects=False,
            data=invalid_body,
            headers={"Content-Type": "application/json"},
        )
        if response.status_code != 422:
            print(
                f"Expected 422 response for /token with body `{invalid_body}`. Got {response.status_code}."
            )
            failures += 1
    return failures


def test_token__success(url):
    failures = 0
    for payload in [{}, 1, ["a", 1, "b"], {"user_id": "12345"}]:
        response = requests.post(
            url,
            allow_redirects=False,
            headers={mix_case("content-type"): "application/json"},
            json=payload,
        )
        if response.status_code != 201:
            print(
                f"Expected 201 response for /token with payload `{payload}`. Got {response.status_code}."
            )
            failures += 1
            continue
        if response.headers["Content-Type"] != "application/json":
            # This case _shouldn't_ happen as there's no need to explicitly set the response header.
            print(
                f"Expected Content-Type response header to be `application/json`. Got {response.headers['Content-Type']}."
            )
            failures += 1
            continue

        body = response.json()
        if ["token"] != list(body.keys()):
            print(
                f"Expected JSON response body to only contain key `token`. Got {body}"
            )
            failures += 1
            continue

        token = jwt.decode(body["token"], verify=False)
        if sorted(token.keys()) != ["data", "exp", "nbf"]:
            print(
                f"Expected token keys to be only data, exp, and nbf. Got {sorted(token.keys())}"
            )
            failures += 1
            continue

        if token["data"] != payload:
            print(f"Expected token['data'] to be `{payload}`. Got {token['data']}")
            failures += 1
            continue
    return failures


if __name__ == "__main__":
    sys.exit(main())
