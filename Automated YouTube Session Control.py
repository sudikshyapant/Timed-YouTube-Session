from selenium import webdriver 
import time
import logging
    
def close_youtube(time_limit = 20):
    
    try:
        logging.basicConfig(level = logging.INFO)
        driver = webdriver.Chrome() 
        driver.get("https://www.youtube.com/")
        time.sleep(5)  

        start_time = time.time()

        #Limit total_time to 900 seconds i.e 15 minutes
        while True:  
            current_elapsed__time = time.time() - start_time
            logging.info(f"Current session time: {current_elapsed__time} seconds" )
            time.sleep(10)
            
            if current_elapsed__time >= time_limit:
                logging.warning("Time limit reached. Closing YouTube.")
                break
            
            time.sleep(1)
    
    except Exception as e:
        logging.info(f"An error occured: {e}")
        
    finally:
        logging.info("Closing browser")
        driver.quit()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    close_youtube()
