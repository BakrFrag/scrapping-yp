import logging
from pymongo import errors
from functools import wraps

logger = logging.getLogger("yp")

def handle_mongo_errors(func):
    """
    warpper decorator to handle mongo db connection errors
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.client:
            print("MongoDB client is not initialized.")
            return None
        try:
            return func(self, *args, **kwargs)
        except errors.PyMongoError as err:
            logger.error(f"mongo db error with connecting {str(err)}")
            return None
    return wrapper
