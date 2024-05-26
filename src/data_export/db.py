import logging
from typing import Dict , List , Any
from datetime import datetime
import pymongo 
from utils import get_config , handle_mongo_errors

logger = logging.getLogger("yp")

class MongoClient:
    """
    handle mongo operation
    insert , read and create colletion
    """
    SERVER_TIME_OUT_SECONDS:int = 5000
    
    def __init__(self):
        self.client_str:str = f"mongodb+srv://{get_config('MONGO_USER')}:{get_config('MONGO_PASSWORD')}@yp.gkzhknp.mongodb.net/?retryWrites=true&w=majority&appName=YP"
        self.dbname:str = get_config("MONGO_DB_NAME")
        self.collection_name:str = get_config("MONGON_COLLECTION_NAME")
        self.client = self.set_mongo_client()
        logger.info("mongo db init connection")
        
    def set_mongo_client(self):
        """
        set mongo client connection
        raises:
            PyMongoError: if mongo connection error happens
        """
        try:
            return pymongo.MongoClient(self.client_str, serverselectiontimeoutms = MongoClient.SERVER_TIME_OUT_SECONDS)
        except pymongo.errors.PyMongoError as err:
            logger.error(f"error setting up mongo db connection {str(err)}")
        
    @handle_mongo_errors
    def database_exists(self) -> bool:
        """
        check if application database exists on not
        returns: bool
            if db exists or not
        raises:
            PyMongoError: if mongo connection error happens
        """
        
        return self.dbname in self.client.list_database_names()
    
    @handle_mongo_errors
    def create_database_if_not_exists(self):
        """
        if db not exists 
        create db and add collection to it
        raises:
            PyMongoError: if mongo connection error happens
        """
        if not self.database_exists():
            db = self.client[self.dbname]
            collection = db[self.collection_name] 
            logger.info("create database and collection")
            
    @handle_mongo_errors
    def get_data_from_collection(self) -> List[Dict[str,str]]:
        """
        get all data from collection and return it 
        returns: List[Dict[str,str]]
            list of documents in collection
        raises:
            PyMongoError: if mongo connection error happens
        """
        if not self.database_exists():
            return []
        
        db = self.client[self.dbname]
        collection = db[self.collection_name]
        documents = collection.find()
        return list(documents)
        
    @handle_mongo_errors
    def insert_bulk_documents(self, documents: List[Dict[str,str]]):
        """
        insert list of bulk documents inside database
        raises:
            PyMongoError: if mongo connection error happens
        """
        self.create_database_if_not_exists()
        collection = self.client[self.dbname][self.collection_name]
        collection.insert_many(documents)
        logger.info("insert extracted data into mongo db")
        
        
    @handle_mongo_errors
    def get_collection_data(self) -> List[Dict[str,str]]:
        """
        get all data from collection
        returns: List[Dict[str,str]]
            list of all documents from the collection
        """
        data_base = self.client[self.dbname]
        collection = data_base[self.collection_name]
        return list(collection.find({}, {"_id": 0}))
        
    @handle_mongo_errors
    def scrape_or_read_directly(self) -> bool:
        """
        check the date between current date and last inserted item date
        returns: bool 
            weather to scrape data or read from db
            
        """
        if not self.database_exists():
            return True 
        
        collection = self.client[self.dbname][self.collection_name]
        last_item = collection.find_one(sort=[("_id", -1)])
        if not last_item:
            return True
        
        if last_item.get("date").date() != datetime.today().date():
            return True 
        
        return False
        
    
        
        
        
        
        