from selenium import webdriver 
import time
    
def close_youtube():
    #Download the Chrome WebDriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
    driver = webdriver.Chrome() 
    driver.get("https://www.youtube.com/")
    time.sleep(5)  

    total_time = 0
    start_time = time.time()

    #Limit total_time to 900 seconds i.e 15 minutes
    while total_time <= 900:  
        total_time = time.time() - start_time
    #Quit the driver, if total_time exceeds 15 minutes
    if total_time > 900:  
        driver.quit()

if __name__ == "__main__":
    close_youtube()
