import time
from selenium.webdriver.common.by import By
from web_driver import driver

def execute(url):
    print("Starting browser and navigating to Moxfield...")
    
    driver.get(url)
    time.sleep(10)
    print("Page loaded, looking for 'View More' button...")
    # Click "View More" button 3 times to load additional decks
    for i in range(3):
        try:
            find_more_button = driver.find_element(By.XPATH, "//button[./span[text()='View More']]")
            find_more_button.click()
            time.sleep(5)  # Wait for new content to load
            print(f"Clicked 'View More' button {i+1}/3")
        except Exception as e:
            print(f"Could not find 'View More' button on attempt {i+1}: {e}")
            break
    
    # Find all anchor tags that contain "deck" in their href
    print("Collecting deck URLs...")
    a_tags = driver.find_elements(By.XPATH, "//a[contains(@href, 'deck')]")
    a_tags = filter(lambda x: not 'public' in x.get_attribute('href'), a_tags)  # Filter out "lists"
    a_tags = filter(lambda x: not 'liked' in x.get_attribute('href'), a_tags)  # Filter out to be signed in to view
    a_tags = filter(lambda x: not 'following' in x.get_attribute('href'), a_tags)  # Filter out user specific data
    deck_urls = []
    
    for a_tag in a_tags:
        href = a_tag.get_attribute('href')
        if href and 'deck' in href:
            deck_urls.append(href)
    
    # Remove duplicates and print results
    unique_deck_urls = list(set(deck_urls))
    print(f"\nFound {len(unique_deck_urls)} unique deck URLs:")
    for url in unique_deck_urls:
        print(url)

    return unique_deck_urls

if __name__ == "__main__":
    try:
        execute()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()