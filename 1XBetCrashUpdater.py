import time
from selenium import webdriver

# Define the URL of the website
url = "https://1xbet.com/en/allgamesentrance/crash"

# Define the path to the chromedriver executable
chromedriver_path = '/path/to/chromedriver'

# Initialize the webdriver with headless mode
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

while True:
    try:
        # Navigate to the website
        driver.get(url)

        # Wait for the multiplier element to appear
        multiplier_element = driver.find_element_by_css_selector('.c-events-table__multiplier')
        while not multiplier_element.is_displayed():
            time.sleep(0.1)

        # Get the multiplier value
        multiplier = float(multiplier_element.text[1:])
        print(f"Multiplier: {multiplier}")

    except Exception as e:
        print(f"Error: {e}")

    # Wait for 1 second before checking again
    time.sleep(1)

# Quit the webdriver
driver.quit()
