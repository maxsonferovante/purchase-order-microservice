from typing import Dict, List

from purchase_order_microservice.infra.database.mongo.settings.connection import MongoConnectionHandler
from purchase_order_microservice.data.interfaces.order_repository_interface import OrderRepositoryInterface


class OrderRepository(OrderRepositoryInterface):
    
    collection_name = "OrderCollection"
    
    @classmethod
    def create_order(cls, order_document: Dict) -> Dict:
        with MongoConnectionHandler() as mongo_connection_handler:
            order_collection = mongo_connection_handler.get_db_connection()[cls.collection_name]
            order_collection.insert_one(order_document)
            return order_document
    
            
    @classmethod
    def get_order(cls, order_id: str) -> Dict:
        with MongoConnectionHandler() as mongo_connection_handler:
            order_collection = mongo_connection_handler.get_db_connection()[cls.collection_name]
            return order_collection.find_one({"order_id": order_id})