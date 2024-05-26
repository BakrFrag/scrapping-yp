from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class ScrapeRequest(BaseModel):
    """
    Scrape model: pydantic model for data validations
    attributes:
        keyword: str mandatory
            search keyword
        number: int mandatory
            number of search result  , number between 30 and 100
    """
    keyword: str
    number: int = Field(..., ge=30, le=100)
    
class ScrapeResponse(BaseModel):
    """
    out model , reprsents data being sent in response 
    attributes:
    """
    title: str
    description: Optional[str]
    address: Optional[str]
    website_url: Optional[str]
    image_url: Optional[str]
    phone_number: Optional[str]
    category: Optional[str]
    date: datetime