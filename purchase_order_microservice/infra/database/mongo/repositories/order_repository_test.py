import pytest
from datetime import datetime
from uuid import uuid4

from purchase_order_microservice.infra.database.mongo.repositories.order_repository import OrderRepository


class TestOrderRepository:


    def test_create_order(self):
        
        order_document = {"order_id": uuid4().__str__(), 
                          "client_id": "1", 
                          "total": 10.0,
                          "items": [{"product_id": "1", "price": 10.0}],
                          "created_at": datetime.now(),
                          "updated_at": datetime.now()   
                          }
        
        order = OrderRepository.create_order(order_document)
        
        assert order == order_document

    def test_get_order(self):
        
        order_id = uuid4().__str__()
        
        order_document = {"order_id": order_id, 
                          "client_id": "1", 
                          "total": 10.0,
                          "items": [{"product_id": "1", "price": 10.0}],
                          "created_at": datetime.now(),
                          "updated_at": datetime.now()   
                          }
        
        OrderRepository.create_order(order_document)
        
        order = OrderRepository.get_order(order_id)
        print (order)
        print (order_document)
        
        assert order.get("order_id") == order_document.get("order_id")
        assert order.get("client_id") == order_document.get("client_id")
        assert order.get("total") == order_document.get("total")
        assert order.get("items") == order_document.get("items")
        