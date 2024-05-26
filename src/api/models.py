from pydantic import BaseModel, Field
from typing import Optional

class ScrapeModel(BaseModel):
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