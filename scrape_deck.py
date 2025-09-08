import time
from selenium.webdriver.common.by import By
from web_driver import driver

def execute(selected_url = "https://moxfield.com/decks/VTVVTgDP3kOSWsZH3Zmd0Q"):
    driver.get(selected_url)
    time.sleep(5)  # Wait for the page to load
    
    more_button = driver.find_element(By.XPATH, "//a[./span[text()='More']]")
    more_button.click()
    time.sleep(2) # Wait for the menu to appear

    export_button = driver.find_element(By.XPATH, "//a[contains(., 'Export')]")
    export_button.click()
    time.sleep(5) # Wait for the export modal to appear

    decklist_textbox = driver.find_element(By.XPATH, "//textarea")
    decklist_text = decklist_textbox.get_attribute("value")
    print(decklist_text)
    
    return decklist_text
    
if __name__ == "__main__":
    execute()
    