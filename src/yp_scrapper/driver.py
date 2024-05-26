import logging
import time
from selenium import webdriver

logger = logging.getLogger("yp")

class DriverManager:
    """
    handle web driver operations 
    like init , quit and get url
    """
    
    def __init__(self):
        """
        init instance variable for web driver
        """
        
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options= self.options)
        
    def get_url(self,url:str):
        """
        get url as web driver
        """
        try:
            self.driver.get(url)
            time.sleep(10)
            logger.info(f"driver get url {url}")
        except Exception as e:
            logger.error(f"while getting driver url exception {str(e)} happens")
        
    def driver_quit(self):
        """
        quit driver
        """
        self.driver.quit()
    
    
                
        