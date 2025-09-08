import scrape_decklist
import scrape_deck
from web_driver import driver

import json
import os
from random import randint
import sys

try:
    custom_url = sys.argv[1]  # Accept custom URL as command line argument
except Exception as e:
    custom_url = False

deck_data_file = "deck_urls.json"
deck_file_exists = os.path.exists(deck_data_file)

def fetch_deck_urls(url=None):
    if not url:
        url = "https://moxfield.com/decks/public?q=eyJodWIiOiIiLCJmb3JtYXQiOiJjb21tYW5kZXIiLCJkZWNrTmFtZSI6IiIsImNhcmRJZCI6IiIsImNhcmROYW1lIjoiIiwiYm9hcmQiOiIiLCJsYXN0U2VhcmNoIjoiIiwiZmlsdGVyIjoiIiwiYXV0aG9yVXNlck5hbWVzIjoiIiwiY29tbWFuZGVyQ2FyZElkIjoiIiwiY29tbWFuZGVyQ2FyZE5hbWUiOiIiLCJwYXJ0bmVyQ2FyZElkIjoiIiwicGFydG5lckNhcmROYW1lIjoiIiwiY29tbWFuZGVyU2lnbmF0dXJlU3BlbGxDYXJkSWQiOiIiLCJjb21tYW5kZXJTaWduYXR1cmVTcGVsbENhcmROYW1lIjoiIiwicGFydG5lclNpZ25hdHVyZVNwZWxsQ2FyZElkIjoiIiwicGFydG5lclNpZ25hdHVyZVNwZWxsQ2FyZE5hbWUiOiIiLCJjb21wYW5pb25DYXJkSWQiOiIiLCJjb21wYW5pb25DYXJkTmFtZSI6IiIsImJyYWNrZXRTZXR0aW5nIjoiZXF1YWxzIiwiYnJhY2tldCI6IiIsInNvcnRDb2x1bW4iOiJ2aWV3cyIsInNvcnREaXJlY3Rpb24iOiJkZXNjZW5kaW5nIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjY0LCJ2aWV3IjoicHVibGljIiwiaHViTmFtZSI6IiJ9"
    deck_urls = scrape_decklist.execute(url)
    with open(deck_data_file, "w") as f:
        json.dump(deck_urls, f, indent=4)

def get_random_deck_url():
    # Load deck URLs from file
    with open(deck_data_file, "r") as f:
        deck_urls = json.load(f)

    # Randomly select a deck URL
    selected_deck_url = deck_urls[randint(0, len(deck_urls) - 1)]
    return selected_deck_url

def get_card_list(deck_url):
    card_text = scrape_deck.execute(deck_url)
    with open("latest_deck.txt", "w", encoding="utf-8") as f:
        f.write(card_text)

    print(f"Your Commander is: {card_text.splitlines()[0]}")

if __name__ == "__main__":
    if not deck_file_exists or custom_url:
        fetch_deck_urls(custom_url)
    get_card_list(get_random_deck_url())
    driver.quit()
