import logging
from typing import List
from fastapi import APIRouter , HTTPException
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
        mongo_connection = MongoClient()
        scrape_or_read:bool = mongo_connection.scrape_or_read_directly()
        if not scrape_or_read:
            logger.info("data already scrapped today - read it directly")
            return mongo_connection.get_collection_data()
        
        logger.debug("old data or not exists start scrapping")
        scrapper = YPScrapper(card_numbers= request_data.number , keyword= request_data.keyword , driver_manager= driver_manager)
        results = scrapper.extract_data()
        logger.debug("data scrapped successfully")
        mongo_connection.insert_bulk_documents(results)
        logger.debug("data inserted into mongo db")
        return results
    except Exception as e:
        logger.error(f"exception while scrape data {str(e)}")
        raise HTTPException(status_code=500, detail = f"failed to scrape data as {str(e)}")