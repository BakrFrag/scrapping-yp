import os
import pymongo 
from dotenv import load_dotenv

load_dotenv()

class MongoClient:
    """
    handle mongo operation
    insert , read and create colletion
    """
    
    def __init__(self):
        self.client:str = f"mongodb+srv://{os.environ.get('MONGO_USER')}:{os.environ.get('MONGO_PASSWORD')}@yp.gkzhknp.mongodb.net/?retryWrites=true&w=majority&appName=YP"
        
    def database_exists(self) -> bool:
        """
        check if application database exists on not
        """
        dbname = os.environ.get("MONGO_DB_NAME")
        if dbname in self.client.list_database_names():
            return True
        return False   
    
     