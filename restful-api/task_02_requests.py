#!/usr/bin/env python3

"""Module to interact with API"""

import requests
import csv


def fetch_and_print_posts():
    """Fetches all post from JSONPlaceholder."""

    url = "https://jsonplaceholder.typicode.com/posts"
    answer = requests.get(url)
    print(f"Status Code: {answer.status_code}")

    if answer.status_code == 200:
        posts = answer.json()
        for post in posts:
            print(post['title'])
    else:
        print("Erreur pendant la récupération des données.")


def fetch_and_save_posts():
    """Fetches all post from JSONPlaceholder."""

    url = "https://jsonplaceholder.typicode.com/posts"
    answer = requests.get(url)

    if answer.status_code == 200:
        posts = answer.json()

        posts_data = []
        for post in posts:
            posts_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)

        print("Données enregistrées dans posts.csv.")
    else:
        print("Erreur lors de l'enregistrement des données.")
