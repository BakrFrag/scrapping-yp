import time
from typing import List , Any
from selenium import webdriver

class DriverManager():
    """
    handle web driver operations 
    like init , quit and get url
    """
    
    CARDS_PER_PAGE:int = 20
    
    def __init__(self, keyword:str, card_numbers:int):
        """
        init instance variable for web driver
        """
        
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options= self.options)
        self.url:str = f'https://yellowpages.com.eg/en/search/{keyword}'
        self.card_numbers:int = card_numbers
        
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
        number_of_pages:int = int((self.card_numbers/self.CARDS_PER_PAGE))+1
        cards:int = self.card_numbers
        for i in range(1,number_of_pages+1):
            if cards <= 20:
                pages.append([f"{self.url}/p{i}",cards])
            else:
                pages.append([f"{self.url}/p{i}",20])
                cards -= 20
        return pages
    
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
    
    
                
        