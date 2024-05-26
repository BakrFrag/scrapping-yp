import os
from pymongo import MongoClient as errors
from functools import wraps

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
            print(f"An error occurred: {err}")
            return None
    return wrapper
