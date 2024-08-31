from bson.objectid import ObjectId
from typing import Dict, List
from purchase_order_microservice.infra.database.mongo.settings.connection import MongoConnectionHandler
from purchase_order_microservice.data.interfaces.order_repository_interface import OrderRepositoryInterface
from purchase_order_microservice.domain.models.order import Order

class OrderRepository(OrderRepositoryInterface):
    
    collection_name = "OrderCollection"
    
    @classmethod
    def create_order(cls, order: Order) -> Order:
        with MongoConnectionHandler() as mongo_connection_handler:
            order_collection = mongo_connection_handler.get_db_connection()[cls.collection_name]
            result = order_collection.insert_one(order.to_dict())
            order.order_id = str(result.inserted_id)
            return order
    
            
    @classmethod
    def get_order_by_id(cls, order_id: str) -> Order:
        with MongoConnectionHandler() as mongo_connection_handler:
            order_collection = mongo_connection_handler.get_db_connection()[cls.collection_name]
            result = order_collection.find_one(
                {
                    "_id": ObjectId(order_id)
                }
            )
            if result:
                result["order_id"] = str(result.get("_id"))
                result.pop("_id")
            return result