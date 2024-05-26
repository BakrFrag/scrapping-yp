from fastapi import APIRouter
from pydantic import ValidationError
from data_export import MongoClient
from yp_scrapper import DriverManager , YPScrapper
from api.models import ScrapeRequest , ScrapeResponse

router = APIRouter()

@router.post("/scrape-yp/", response_model=ScrapeResponse, tags=["scraping"])
async def scrape_yp(request_data: ScrapeRequest):
    """
    scrape endpoint handle scrapping results and save it 
    in_model:
        ScrapeRequest 
    response_model:
        ScrapeResponse
    """
    try:
        driver_manager = DriverManager()
        mongo_connection = MongoClient()
        scrapper = YPScrapper(card_numbers= request_data.number , keyword= request_data.keyword , driver_manager= driver_manager)
        results = scrapper.extract_data()
        mongo_connection.insert_bulk_documents(results)
    except Exception as e:
        print(str(e))
    

