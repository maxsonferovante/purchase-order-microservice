import pytest
from datetime import datetime

from purchase_order_microservice.infra.database.mongo.repositories.order_repository import OrderRepository


class TestOrderRepository:


    def test_create_order(self):
        
        order_document = { 
                          "client_id": "1", 
                          "total": 10.0,
                          "product_list": [{"product_id": "1", "name": "product 1", "price": 10.0}],
                          "created_at": datetime.now(),
                          "updated_at": datetime.now()   
                          }
        
        order = OrderRepository.create_order(order_document)
        
        assert order.get("order_id") is not None
        assert order.get("client_id") == order_document.get("client_id")
        assert order.get("total") == order_document.get("total")
        assert order.get("product_list") == order_document.get("product_list")

    def test_get_order_by_id(self):
        
        order_document = { 
                          "client_id": "1", 
                          "total": 10.0,
                          "product_list": [{"product_id": "1", "name": "product 1", "price": 10.0}],
                          "created_at": datetime.now(),
                          "updated_at": datetime.now()   
                          }
        
        order_document_created = OrderRepository.create_order(order_document)
                
        order = OrderRepository.get_order_by_id(order_id=order_document_created.get("order_id"))
        
        assert order.get("order_id") == order_document.get("order_id")
        assert order.get("client_id") == order_document.get("client_id")
        assert order.get("total") == order_document.get("total")
        assert order.get("items") == order_document.get("items")
        