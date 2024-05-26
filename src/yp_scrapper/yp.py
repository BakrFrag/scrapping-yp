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
        
    def get_tilte(self , card):
        """
        extract title from card
        """
        item_title = card.find_element(By.CLASS_NAME , "item-title")
        return item_title.text.strip()
        