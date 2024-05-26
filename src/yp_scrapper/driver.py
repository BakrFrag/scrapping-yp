import time
from selenium import webdriver

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
        
        self.driver.get(url)
        time.sleep(10)
        
    def driver_quit(self):
        """
        quit driver
        """
        self.driver.quit()
    
    
                
        