#!/usr/bin/python3
"""
Module that fetches and processes data from JSONPlaceholder API
using the requests library.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder API and print their titles.

    Prints the HTTP status code.
    If the request is successful (status code 200),
    parses the JSON response and prints the title of each post.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder API and save them to a CSV file.

    If the request is successful (status code 200),
    structures the data into a list of dictionaries
    containing only id, title, and body fields.
    Writes the data into 'posts.csv'.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open("posts.csv", mode="w",
                  newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()
            writer.writerows(structured_posts)
