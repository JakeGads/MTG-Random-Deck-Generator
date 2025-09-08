import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Set up Chrome options for better performance and reliability
options = Options()
# chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
# Add an argument to make output nonverbose
options.add_argument("--log-level=3") 

driver = None
for i in [webdriver.Chrome, webdriver.Firefox, webdriver.Edge, webdriver.Safari]:
    try:
        driver = i(options=options)
        break
    except Exception as e:
        print(f"Could not start {i}: {e}")
        continue