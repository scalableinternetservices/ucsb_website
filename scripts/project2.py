#!/usr/bin/env python3
import hashlib
import random
import re
import sys
from urllib.parse import urljoin, urlparse

import requests


CONTENT_TYPES = [
    "application/json",
    "application/octet-stream",
    "audio/mpeg",
    "image/gif",
    "image/jpeg",
    "image/png",
    "text/css;charset=utf-8",
    "text/html;charset=utf-8",
    "text/javascript;charset=utf-8",
    "text/plain;charset=utf-8",
]
RE_HEXDIGEST = re.compile(r"\A[a-z0-9]{64}\Z")
MAX_FILESIZE = 1024 * 1024


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
    issues = 0

    result = urlparse(url)
    if result.scheme != "https":
        print(f"Scheme is not https: {result.scheme}")
        issues += 1

    if not result.netloc.endswith("-fi6eeq56la-uc.a.run.app"):
        print(f"Domain does not appear to be google cloud run: {result.netloc}")
        issues += 1

    if result.path not in ["", "/"]:
        print(f"Resource path must be `/`. Yours: {result.path}")
        issues += 1

    issues += test_root_url(url)
    issues += test_files__invalid_create(url)
    issues += test_files__invalid_get_and_delete(url)
    issues += test_files__duplicate_create(url)
    issues += test_files__create_get_list_delete(url)

    if issues == 0:
        print("Passed")
    else:
        print(count_format("Issue", issues))
    return issues


def test_files__create_get_list_delete(url):
    issues = 0

    files_url = urljoin(url, "/files/")
    content_type = random.choice(CONTENT_TYPES)
    body = bytearray(random.getrandbits(8) for _ in range(MAX_FILESIZE))

    # Create the file
    response = requests.post(
        files_url, files={"file": (random.choice(WORDS), body, content_type)}
    )
    if response.status_code != 201:
        print(
            f"Expected 201 response for `POST {files_url}`. Got {response.status_code}."
        )
        return 1
    digest = response.json()["uploaded"]
    expected_digest = hashlib.sha256(body).hexdigest()
    if digest != expected_digest:
        print(f"`{digest}` does not match expected: {expected_digest}")
        return 1

    # Fetch the file
    file_url = urljoin(files_url, mix_case(digest))
    response = requests.get(file_url)
    if response.status_code != 200:
        print(
            f"Expected 200 response for `GET {file_url}`. Got {response.status_code}."
        )
        return 1
    if response.headers["Content-Type"] != content_type:
        print(
            f"Expected Content-Type to be `{content_type}`. Got {response.headers['Content-Type']}"
        )
        issues += 1
    if response.content != body:
        print("Body does not match")
        issues += 1

    # List files
    response = requests.get(files_url)
    if response.status_code != 200:
        print(
            f"Expected 200 response for `GET {files_url}`. Got {response.status_code}."
        )
        return 1
    digests = response.json()
    if sorted(digests) != digests:
        print("File list is not in sorted order")
        issues += 1
    if digest not in digests:
        print(
            f"Could not find {digest} in list of {count_format('digest', len(digests))} after create"
        )
        issues += 1
    for tmp_digest in digests:
        if not RE_HEXDIGEST.match(tmp_digest):
            print(f"`{tmp_digest}` is not a valid sha256 hex digest")
            issues += 1

    # Delete file
    file_url = urljoin(files_url, mix_case(digest))
    response = requests.delete(file_url)
    if response.status_code != 200:
        print(
            f"Expected 200 response for `DELETE {file_url}`. Got {response.status_code}."
        )
        issues += 1

    # List files
    response = requests.get(files_url)
    if response.status_code != 200:
        print(
            f"Expected 200 response for `GET {files_url}`. Got {response.status_code}."
        )
        return 1
    files = set(response.json())
    if digest in files:
        print(
            f"Found {digest} in list of {count_format('file', len(files))} after delete"
        )
        issues += 1

    # Duplicate delete file to verify idempotency
    response = requests.delete(file_url)
    if response.status_code != 200:
        print(
            f"Expected 200 response for `DELETE {file_url}`. Got {response.status_code}."
        )
        issues += 1

    # Fetch the no longer existing file
    file_url = urljoin(files_url, mix_case(digest))
    response = requests.get(file_url)
    if response.status_code != 404:
        print(
            f"Expected 404 response for `GET {file_url}`. Got {response.status_code}."
        )
        issues += 1

    return issues


def test_files__duplicate_create(url):
    files_url = urljoin(url, "/files/")
    content_type = random.choice(CONTENT_TYPES)
    body = str(random.random()).encode("utf-8")

    # Create the file
    response = requests.post(
        files_url, files={"file": (random.choice(WORDS), body, content_type)}
    )
    if response.status_code != 201:
        print(
            f"Expected 201 response for `POST {files_url}`. Got {response.status_code}."
        )
        return 1
    digest = response.json()["uploaded"]
    expected_digest = hashlib.sha256(body).hexdigest()
    if digest != expected_digest:
        print(f"`{digest}` does not match expected: {expected_digest}")
        return 1

    # Recreate the file
    response = requests.post(
        files_url, files={"file": (random.choice(WORDS), body, content_type)}
    )
    if response.status_code != 409:
        print(
            f"Expected 409 response for `POST {files_url}`. Got {response.status_code}."
        )
        return 1
    return 0


def test_files__invalid_create(url):
    files_url = urljoin(url, "/files/")
    issues = 0

    for data in [None, {"file": ""}, {"file": "file"}, {"file": "tempfile"}]:
        response = requests.post(files_url, data=data)
        if response.status_code != 422:
            print(
                f"Expected 422 response for `POST {files_url}`. Got {response.status_code}."
            )
            issues += 1

    response = requests.post(files_url, files={"data": (random.choice(WORDS), "body")})
    if response.status_code != 422:
        print(
            f"Expected 422 response for `POST {files_url}`. Got {response.status_code}."
        )
        issues += 1

    body = bytearray(random.getrandbits(8) for _ in range(MAX_FILESIZE + 1))
    response = requests.post(
        files_url,
        files={"file": (random.choice(WORDS), body, random.choice(CONTENT_TYPES))},
    )
    if response.status_code != 422:
        print(
            f"Expected 422 response for `POST {files_url}`. Got {response.status_code}."
        )
        issues += 1

    return issues


def test_files__invalid_get_and_delete(url):
    issues = 0

    for method in ["GET", "DELETE"]:
        digest = ""
        while "0" not in digest:
            digest = hashlib.sha256(str(random.random()).encode("utf-8")).hexdigest()
        for invalid in [digest[:-1], digest + "a", digest.replace("0", "g")]:
            files_url = urljoin(url, f"/files/{invalid}")
            response = requests.request(method, files_url)
            if response.status_code != 422:
                print(
                    f"Expected 422 response for `{method} {files_url}`. Got {response.status_code}."
                )
                issues += 1
    return issues


def test_root_url(url):
    response = requests.get(url, allow_redirects=False)
    if response.status_code != 302:
        return 1
    return (
        0 if response.headers["Location"] in ["/files/", urljoin(url, "/files/")] else 1
    )


if __name__ == "__main__":
    sys.exit(main())
