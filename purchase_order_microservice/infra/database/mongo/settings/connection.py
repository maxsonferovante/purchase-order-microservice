import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class MongoConnectionHandler:
    def __init__(self):
        
        self.__connection_string = self.__create_connection_string()        
        self.__database_name = os.getenv("MONGO_DB")
        self.__client = None
        self.__db_connection = None
        
        self.__connect_to_db()
        
    def __create_connection_string(self) -> str:
    
        url = "{}://{}:{}@{}:{}/?authSource=admin".format(
            os.getenv("MONGO_PROTOCOL") or "mongodb",
            os.getenv("MONGO_USER"),
            os.getenv("MONGO_PASSWORD"),
            os.getenv("MONGO_HOST"),
            os.getenv("MONGO_PORT") or "27017",
        )
        return url    
        
    def __connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]
    
    def get_client(self) -> MongoClient:
        return self.__client
        
    def get_db_connection(self) -> MongoClient:
        return self.__db_connection
    
    def __enter__(self) -> MongoClient:
        return self
    
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.__client = None
        self.__db_connection = None
    
    

    