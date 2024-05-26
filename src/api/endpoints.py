import logging
from typing import List
from fastapi import APIRouter
from data_export import MongoClient
from yp_scrapper import DriverManager , YPScrapper
from api.models import ScrapeRequest , ScrapeResponse

logger = logging.getLogger("yp")
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
        
        logger.debug(f"received request to scrape yp with {request_data.keyword} with number {request_data.number}")
        driver_manager = DriverManager()
        logger.debug("driver manager init")
        mongo_connection = MongoClient()
        logger.debug(f"mongo connection init")
        scrapper = YPScrapper(card_numbers= request_data.number , keyword= request_data.keyword , driver_manager= driver_manager)
        results = scrapper.extract_data()
        logger.debug("data scrapped well")
        mongo_connection.insert_bulk_documents(results)
        logger.debug("data inserted into mongo db")
        return results
    except Exception as e:
        logger.error(f"exception while scrape data {str(e)}")