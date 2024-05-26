import os
import pymongo 
from dotenv import load_dotenv
from utils.wrappers import handle_mongo_errors
load_dotenv()

class MongoClient:
    """
    handle mongo operation
    insert , read and create colletion
    """
    SERVER_TIME_OUT_SECONDS:int = 5000
    
    def __init__(self):
        self.client_str:str = f"mongodb+srv://{os.environ.get('MONGO_USER')}:{os.environ.get('MONGO_PASSWORD')}@yp.gkzhknp.mongodb.net/?retryWrites=true&w=majority&appName=YP"
        self.dbname:str = os.environ.get("MONGO_DB_NAME")
        self.collection_name:str = os.environ.get("MONGON_COLLECTION_NAME")
        self.client = pymongo.MongoClient(self.client_str, seMverSelectionTimeoutMS = MongoClient.SERVER_TIME_OUT_SECONDS)
        
    @handle_mongo_errors
    def database_exists(self) -> bool:
        """
        check if application database exists on not
        """
        
        return self.dbname in self.client.list_database_names()
    
    @handle_mongo_errors
    def create_database_if_not_exists(self):
        """
        if db not exists 
        create db and add collection to it
        """
        if not self.database_exists(self.dbname):
            db = self.client[self.dbname]
            collection = db[self.collection_name] 