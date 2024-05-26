import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from yp_scrapper.driver import DriverManager
class Scrapper():
    """
    scrape yellow pages 
    extract info from cards and return data
    """
    
    def __init__(self, driver_manager:DriverManager):
        self.driver_manager = driver_manager
        
    def get_tilte(self , card) -> str:
        """
        extract title from card
        returns: str
            card title

        """
        item_title = card.find_element(By.CLASS_NAME , "item-title")
        return item_title.text.strip()
    
    def get_description(self, card) -> str:
        """
        extract description form card 
        returns: str 
            text description seprated by space
        """
        try:
            item_description = card.find_element(By.CLASS_NAME , "item-aboutUs")
            item_text = item_description.find_element(By.TAG_NAME , "a")
            description = item_text.text.split()
            return " ".join(description)
        except:
            return "N/A"
        
    
        