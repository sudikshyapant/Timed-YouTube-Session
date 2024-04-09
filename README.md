# Timed-YouTube-Session

This Python script automates the process of closing the YouTube web page after a specified time duration, helping users manage their screen time effectively.

## Requirements
Python 3.x
Selenium library
Chrome WebDriver (download from https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Installation
1. Install Python 3.x from the official website.
2. Install the Selenium library using pip:
pip install selenium
3. Download the Chrome WebDriver from the provided link and place it in your PATH.

## Usage
Clone or download this repository to your local machine.
Run the code.

## Code

from selenium import webdriver
import time
def close_youtube():
    driver = webdriver.Chrome()  # Path to Chrome WebDriver
    driver.get("https://www.youtube.com/")
    time.sleep(5)  # Wait for the page to load

    total_time = 0
    start_time = time.time()

    while total_time <= 900:  # Limit total_time to 900 seconds (15 minutes)
        total_time = time.time() - start_time
       
    if total_time > 900:  # If total_time exceeds 15 minutes, quit the driver
        driver.quit()

if __name__ == "__main__":
    close_youtube()    
    
## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request with your enhancements.

## License
This project is licensed under the MIT License.
