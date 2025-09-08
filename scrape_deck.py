import time
from selenium.webdriver.common.by import By
from web_driver import driver
import os
def execute(selected_url = "https://moxfield.com/decks/VTVVTgDP3kOSWsZH3Zmd0Q"):
    driver.get(selected_url)
    time.sleep(5)  # Wait for the page to load
    deck_name = driver.find_element(By.TAG_NAME, "h1").text

    more_button = driver.find_element(By.XPATH, "//a[./span[text()='More']]")
    more_button.click()
    time.sleep(2) # Wait for the menu to appear

    export_button = driver.find_element(By.XPATH, "//a[contains(., 'Export')]")
    export_button.click()
    time.sleep(5) # Wait for the export modal to appear

    decklist_textbox = driver.find_element(By.XPATH, "//textarea")
    decklist_text = decklist_textbox.get_attribute("value")
    print(decklist_text)

    # Clean the deck_name to be safe for use as a filename
    deck_name = "".join([c for c in deck_name if c.isalnum() or c in (' ', '_')]).rstrip()

    os.makedirs("fetched decks", exist_ok=True)
    with open(f"fetched decks/{deck_name}.md", "w", encoding="utf-8") as f:
        f.write(f"# {deck_name}\n\n")
        f.write("---\n\n")
        f.write("url: " + selected_url + "\n\n")
        f.write("---\n\n")
    
        for line in decklist_text.splitlines():
            f.write(line + "\n\n")
    
    return decklist_text
    
if __name__ == "__main__":
    execute()
    