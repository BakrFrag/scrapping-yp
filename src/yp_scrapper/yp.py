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
        
    def get_phone_number(self, card) -> str:
        """
        extract phone number if exists 
        hints:
            phone number not shown until click , waits for 1 second for data render
        returns: str 
            phone number value
        """
        
        try:
            callback_us_element = card.find_element(By.CLASS_NAME, 'call-us-click')
            callback_us_element.click()
            time.sleep(1)
            data_content = callback_us_element.get_attribute('data-content')
            return data_content.split('tel:')[1].split('"')[0] if 'tel:' in data_content else 'N/A'
        except:
            return "N/A"
        
    def get_address(self, card) -> str:
        """
        extract address if exists
        returns: str 
            address extract
        """
        try:
            item_addres = card.find_element(By.CLASS_NAME , "address-text")
            address = item_addres.text.split()
            return " ".join(i for i in address)
        except:
            return "N/A"
            
    def get_website_url(self,card) -> str:
        """
        get website url
        returns: str 
            website url
        """
        try:
            website = card.find_element(By.CLASS_NAME, 'website')
            return website.get_attribute("href")
        except:
            return "N/A"
        
    def get_category(self, card) -> str:
        """
        extract category 
        returns: str 
            categories
        """
        try:
            category = category.find_element(By.CLASS_NAME , "category")
            category = category.find_element(By.TAG_NAME , "a")
            return " ".join(category.text.split())
        except:
            return "N/A"
        
    def get_company_logo(self, card) -> str:  
        """
        extract card image url
        returns: str 
            card logo url
        """
        try:
            logo_container = card.find_element(By.CLASS_NAME , "logo-container")
            image = logo_container.find_element(By.TAG_NAME , "img")
            image_url = image.get_attribute("src")  or image.get_attribute("data-src") 
            image_url = image_url if image_url.startswith("https://") else  f"https://{image_url}"
            return image_url
        
        except:
            return "N/A"
        
        
    
        