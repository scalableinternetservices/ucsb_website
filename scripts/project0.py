#!/usr/bin/env python3
import sys
from urllib.parse import urljoin, urlparse

import requests
from html5_parser import parse


def count_format(word, number):
    base = f"{number} {word}"
    if number != 1:
        base += "s"
    return base


def main():
    if len(sys.argv) == 1:
        local_file = 'example.html'
        print(f'No args given, scoring local file {local_file}')
        content = open(local_file,'r').read()
        return page_issues(content, 'file:///'+local_file)

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} URL")
        return 1

    return score(url=sys.argv[1])


def page_issues(content, url):
    issues = 0
    root = parse(content, sanitize_names=False)
    tags = list(root.iterdescendants())

    base_tags = [x for x in tags if x.tag == "base"]
    if len(base_tags) > 1:
        print("Cannot have more than one base tag")
        return 1
    elif len(base_tags) == 1:
        base_href = base_tags[0].attrib["href"]
        if base_href.startswith("/"):
            base_url = base_href
        else:
            base_url = urljoin(url, base_href)
    else:
        base_url = url

    a_tags = [x for x in tags if x.tag == "a"]
    for a_tag in a_tags:
        if not (a_tag.text or list(a_tag.iterdescendants())):
            print("Found empty a tag")
            issues += 1
            continue
        if a_tag.attrib["href"].startswith("https://github.com/"):
            break
    else:
        print("No link back to github repository found")
        issues += 1

    h1_tags = [x for x in tags if x.tag == "h1"]
    if not h1_tags:
        print("No h1 tag found")
        issues += 1
    for h1_tag in h1_tags:
        if len(h1_tag.text) < 1:
            print("Found empty H1 tag")
            issues += 1

    image_tags = [x for x in tags if x.tag == "img"]
    if image_tags:
        for image_tag in image_tags:
            src = image_tag.attrib["src"]
            image_url = urljoin(base_url, src)
            if image_url.startswith(url):
                response = requests.head(image_url, allow_redirects=False)
                if response.status_code == 200:
                    break
                print(f"Broken img src: {image_url}")
                issues += 1
        else:
            print(
                f"Found {count_format('image', len(image_tags))}, but no local img src found."
            )
            issues += 1
    else:
        print("No img tag found")
        issues += 1

    link_tags = [x for x in tags if x.tag == "link"]
    if link_tags:
        for link_tag in link_tags:
            rel = link_tag.attrib["rel"].lower()
            if rel == "stylesheet":
                href = link_tag.attrib["href"]
                css_url = urljoin(base_url, href)
                if css_url.startswith(url):
                    response = requests.head(css_url, allow_redirects=False)
                    if response.status_code == 200:
                        break
                    print(f"Broken link href: {css_url}")
                    issues += 1
        else:
            print(
                f"Found {count_format('link', len(link_tags))}, but no local link href stylesheets found."
            )
            issues += 1
    else:
        print("No link tag found")
        issues += 1

    table_tags = [x for x in tags if x.tag == "table"]
    if table_tags:
        pass
    else:
        print("No table tag found")
        issues += 1

    title_tags = [x for x in tags if x.tag == "title"]
    if len(title_tags) != 1:
        print("Must have exactly one title tag")
        issues += 1
    elif len(title_tags[0].text) < 4:
        print("Title text cannot be blank")
        issues += 1

    ul_tags = [x for x in tags if x.tag == "ul"]
    if ul_tags:
        pass
    else:
        print("No ul tag found")
        issues += 1

    return issues


def score(url):
    result = urlparse(url)
    failures = 0
    if result.scheme != "https":
        print(f"Scheme is not https: {result.scheme}")
        failures += 1

    if not result.netloc.endswith("github.io"):
        print(f"Domain does not appear to be github: {result.netloc}")
        return failures + 1  # Cannot continue

    response = requests.get(url)
    if response.status_code != 200:
        print(f"URL responded with non 200 status: {response.status_code}")
        return failures + 1  # Cannot continue
    content = response.content

    if response.history:
        print("URL redirected more than 0 times:")
        for history in response.history:
            print(f"\t{history.url} -> {history.headers['location']}")
        failures += 1

    # html_validation_url = f"https://validator.w3.org/nu/"
    # response = requests.get(html_validation_url, params={"doc": url, "out": "json"})
    # if response.status_code != 200:
    #     print(f"HTML validation unexpectedly failed: {response.status_code}")
    #     return 1
    # messages = response.json()['messages']
    # if messages:
    #     print("HTML5 validation had some issues:")
    #     for message in messages:
    #         print(f"\t{message['type']}: {message['message']}")
    #     return failures + len(messages)

    failures += page_issues(content, url)

    if failures == 0:
        print("Passed")
    else:
        print(count_format("Failure", failures))
    return failures


if __name__ == "__main__":
    sys.exit(main())
