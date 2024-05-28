import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Define the URL of the website
url = "https://1xbet.com/en/allgamesentrance/crash"
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') 
chrome_options.add_argument('--disable-dev-shm-usage') 


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

while True:
    try:
        # Navigate to the website
        driver.get(url)
        multiplier_element = driver.find_element(By.CSS_SELECTOR,'.c-events-table__multiplier')
        
        while not multiplier_element.is_displayed():
            time.sleep(0.1)

        # Get the multiplier value
        multiplier = float(multiplier_element.text[1:])
        print(f"Multiplier: {multiplier}")

    except Exception as e:
        print(f"Error: {e}")
    time.sleep(1)
driver.quit()
