import time
from typing import List , Any , Dict
from selenium import webdriver
from selenium.webdriver.common.by import By 
from yp_scrapper.driver import DriverManager


class Scrapper():
    """
    scrape yellow pages 
    extract info from cards and return data
    """
    CARDS_PER_PAGE:int = 20
    BASE_URL:str = "https://yellowpages.com.eg/en/search/"
    
    def __init__(self, card_numbers:int , keyword:str, driver_manager:DriverManager):
        self.card_numbers = card_numbers
        self.keyword = keyword
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
            image_url_with_https = image_url if image_url.startswith("https://") else  f"https://{image_url}"
            return image_url_with_https
        
        except:
            return "N/A"
        
        
    def define_pages(self) ->List[Any]:
        """
        for pagination handling
        define number of pages to be scrapped and number of results being extracted 
        per each page
        
        return: List[List[str, int]]
            list of lists , inner list include str reprsents page url and int include number of card info being extracted
        """
        
        if self.card_numbers <= 20:
            return [self.url, self.card_numbers]
        pages:List = []
        number_of_pages:int = int((self.card_numbers/Scrapper.CARDS_PER_PAGE))+1
        cards:int = self.card_numbers
        for i in range(1,number_of_pages+1):
            if cards <= 20:
                pages.append([f"{Scrapper.BASE_URL}/{self.keyword}/p{i}",cards])
            else:
                pages.append([f"{self.url}/p{i}",20])
                cards -= 20
        return pages
    
    def extract_data(self) -> List[Dict[str, str]]:
        """
        extract info from each page
        returns: List[Dict[str, str]]
            return list of dict , each dict include 
            phone_address: str  phone number
            category: str category info 
            description: str text include description
            title: str title
            image_url: str logo url 
            website_url: str include web site url
            address: str address
        """
        pages_with_results = self.define_pages()
        scrapping_results:List[Dict[str,str]] = [] 
        for page in pages_with_results:
            (url , result_counter) = page[0] , page[1]
            self.driver_manager.get(url)
            row_data_elements = self.driver_manager.driver.find_elements(By.CSS_SELECTOR, '.row.item-row:not(.search-ads)')
            number_of_results:int = 0
            for row in row_data_elements:
                scrapped_data:Dict[str,str] = {
                    "title": self.get_tilte(row),
                    "description": self.get_description(row),
                    "address": self.get_address(row),
                    "image_url": self.get_company_logo(row),
                    "website_url": self.get_website_url(row),
                    "category": self.get_category(row),
                    "phone_address": self.get_phone_number(row)
                }
                number_of_results += 1
                scrapping_results.apped(scrapped_data)
                if number_of_results >= result_counter:
                    break
        return scrapping_results
                    
        
        
    
        