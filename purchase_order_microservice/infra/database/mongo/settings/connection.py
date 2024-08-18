import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class MongoConnectionHandler:
    def __init__(self):
        
        self.__connection_string = self.__create_connection_string()
        
        self.__client = self.__create_client()
        
    def __create_connection_string(self) -> str:
        url = "{}://{}:{}@{}/{}".format(
            os.getenv("MONGO_PROTOCOL"),
            os.getenv("MONGO_USER"),
            os.getenv("MONGO_PASSWORD"),
            os.getenv("MONGO_HOST"),
            os.getenv("MONGO_DB")
        )
        return url
    
    def __create_client(self) -> MongoClient:
        return MongoClient(self.__connection_string)
    
    def get_client(self) -> MongoClient:
        return self.__client
    
    def close_connection(self):
        self.__client.close()
        
    def __enter__(self) -> MongoClient:
        return self
    
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.__client = None
    
    

    