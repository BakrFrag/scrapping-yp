from typing import List
from fastapi import APIRouter
from pydantic import ValidationError
from data_export import MongoClient
from yp_scrapper import DriverManager , YPScrapper
from api.models import ScrapeRequest , ScrapeResponse

router = APIRouter()

@router.post("/scrape-yp/", response_model= List[ScrapeResponse], tags=["scraping"])
async def scrape_yp(request_data: ScrapeRequest):
    """
    scrape endpoint handle scrapping results and save it 
    in_model:
        ScrapeRequest 
    response_model:
        ScrapeResponse
    """
    try:
        print(f" received request scrape data with {request_data.number} and {request_data.keyword}")
        driver_manager = DriverManager()
        print("define driver manager")
        mongo_connection = MongoClient()
        print("define mongo connection")
        scrapper = YPScrapper(card_numbers= request_data.number , keyword= request_data.keyword , driver_manager= driver_manager)
        print("scrapper init")
        results = scrapper.extract_data()
        print(results)
        print("data extracted")
        mongo_connection.insert_bulk_documents(results)
        print("data inserted into mongo db")
        return results
    except Exception as e:
        import sys
        print(sys.exc_info())
        
    

