import json
import requests
from bs4 import BeautifulSoup
import os
import markdown
import pprint
import re
import pathlib
import sys


def convert_md_to_dict(md_content):
    # Extract the title, subtitle, author, datePosted, tags, and content fields
    title = re.search(r"^# (.*)", md_content, re.MULTILINE).group(1).strip()
    subtitle = re.search(r"^## (.*)", md_content, re.MULTILINE).group(1).strip()
    author = re.search(r"^### (.*)", md_content, re.MULTILINE).group(1).strip()
    datePosted = re.search(r"^#### (.*)", md_content, re.MULTILINE).group(1).strip()
    tags = (
        re.search(r"^##### (.*)", md_content, re.MULTILINE).group(1).strip().split(",")
    )

    pattern = r"^##### .+\n"
    content_start = re.search(pattern, md_content, flags=re.MULTILINE).end()
    content = md_content[content_start:]
    content = content.strip()

    # Create a dictionary with the extracted fields
    post = {
        "id": title.replace(" ", "-").lower(),
        "title": title,
        "subtitle": subtitle,
        "author": author,
        "date": datePosted,
        "tags": tags,
        "content": content,
    }

    return post


def main():
    secret_key = sys.argv[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer private-" + secret_key,
    }
    url = "https://develop.ent.northamerica-northeast1.gcp.elastic-cloud.com/api/as/v1/engines/blog/documents"

    # set the path to the folder containing the markdown posts
    folder_path = pathlib.Path("blog")
    posts = list()

    # get a list of all the markdown files in the folder
    markdown_files = [f for f in folder_path.iterdir() if f.name.endswith(".md")]

    # loop through the markdown files
    for markdown_file in markdown_files:
        # open the markdown file and read its contents
        with open(os.path.join(folder_path, markdown_file), "r") as f:
            markdown_content = f.read()

        # print the HTML content
        post = convert_md_to_dict(markdown_content)
        posts.append(post)

    response = requests.post(url, headers=headers, data=json.dumps(posts))
    results = response

    print(results.json)

    query = {
        "query": {
            "terms": {
                "_id": [
                    "what-is-the-carbon-footprint-of-digital-currency-and-cryptocurrency?",
                    "what-is-tether-(usdt)?",
                ]
            }
        }
    }

    getpost = requests.get(
        url,
        headers=headers,
        # data=json.dumps(query)
        json=[
            "what-is-the-carbon-footprint-of-digital-currency-and-cryptocurrency?",
            "what-is-tether-(usdt)?",
        ],
    )

    print(len(getpost.json()))


if __name__ == "__main__":
    main()
