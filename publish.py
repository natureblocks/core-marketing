import json
import requests
from bs4 import BeautifulSoup
import os
import markdown
import pprint
import re
import pathlib
import sys
import argparse


def convert_md_to_dict(md_content):
    """Extracts the title, subtitle, author, date, tags, and content from markdown file.

    Parameters
    ----------
    md_content : str.
        To be parsed using regex for blog post schema fields.

    Returns
    -------
    dict.
        Of all required fields for blog post schema.
    """

    title = re.search(r"^# (.*)", md_content, re.MULTILINE).group(1).strip()
    subtitle = re.search(r"^## (.*)", md_content, re.MULTILINE).group(1).strip()
    author = re.search(r"^### (.*)", md_content, re.MULTILINE).group(1).strip()
    date = re.search(r"^#### (.*)", md_content, re.MULTILINE).group(1).strip()
    tags = (
        re.search(r"^##### (.*)", md_content, re.MULTILINE).group(1).strip().split(",")
    )

    pattern = r"^##### .+\n"
    content_start = re.search(pattern, md_content, flags=re.MULTILINE).end()
    content = md_content[content_start:]
    content = content.strip()

    post = {
        "id": title.replace(" ", "-").lower(),
        "title": title,
        "subtitle": subtitle,
        "author": author,
        "date": date,
        "tags": tags,
        "content": content,
    }

    return post


def main():
    """ Loop through all markdown files in the blog folder and convert them to a list of dictionaries. 
    Then, send a POST request to the App Search API to index the blog posts.

     Parameters
    ----------
    api_key : str.
        Used to access Elastic App Search API.
    """
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument("api_key", help="the name of the file to process")
    args = parser.parse_args()
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer private-" + args.api_key,
    }
    url = "https://develop.ent.northamerica-northeast1.gcp.elastic-cloud.com/api/as/v1/engines/blog/documents"


    folder_path = pathlib.Path("blog")

    posts = list()

    # get a list of all the markdown files in the folder
    markdown_files = [f for f in folder_path.iterdir() if f.name.endswith(".md")]

    for markdown_file in markdown_files:
        # open the markdown file and read its contents
        with open(os.path.join('', markdown_file), "r") as f:
            markdown_content = f.read()

        post = convert_md_to_dict(markdown_content)
        posts.append(post)

    response = requests.post(url, headers=headers, data=json.dumps(posts))
    results = response

    print(results.json())


if __name__ == "__main__":
    main()
