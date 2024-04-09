from selenium import webdriver
import time
    
def close_youtube():
    driver = webdriver.Chrome()  # You may need to download the Chrome WebDriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
    driver.get("https://www.youtube.com/")
    time.sleep(5)  # Wait for the page to load

    total_time = 0
    start_time = time.time()

    while total_time <= 900:  # Limit total_time to 900 seconds i.e 15 minutes
        total_time = time.time() - start_time
       
    if total_time > 900:  # If total_time exceeds 15 minutes, quit the driver
        driver.quit()

if __name__ == "__main__":
    close_youtube()
