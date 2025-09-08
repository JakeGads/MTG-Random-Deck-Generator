# MTG Random Deck Generator

A Python tool that scrapes MTG Commander decks from Moxfield and randomly selects one for you to play.

## Features

- Scrapes deck URLs from Moxfield's public deck database
- Randomly selects a deck from the collected URLs
- Extracts and displays the deck's card list
- Shows the First Card (Commander if thats your format)

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv env
   ```
3. Activate the virtual environment:
   - Windows: `env\Scripts\activate`
   - Mac/Linux: `source env/bin/activate`
4. Install dependencies:
   ```bash
   pip install .
   ```

## Usage

Run the main script:
```bash
python main.py
```

Or with a custom Moxfield URL:
```bash
python main.py "https://moxfield.com/decks/public?q=your_custom_query"
```

## Requirements

- Python 3.8+
- Chrome browser (for Selenium WebDriver)
- Selenium 4.0+

## Files

- `main.py` - Main application entry point
- `scrape_moxfield.py` - Scrapes deck URLs from Moxfield
- `scrape_decklist.py` - Module for scraping deck lists
- `scrape_deck.py` - Module for scraping individual decks
- `web_driver.py` - WebDriver configuration
- `deck_urls.json` - Cached deck URLs
- `latest_deck.txt` - Most recently selected deck's card list
