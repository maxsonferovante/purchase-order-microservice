import pytest

from connection import MongoConnectionHandler

class TestMongoConnectionHandler:
    def test_instance(self):
        mongo_connection_handler = MongoConnectionHandler()
        assert isinstance(mongo_connection_handler, MongoConnectionHandler)
        
    def test_get_client(self):
        mongo_connection_handler = MongoConnectionHandler()
        client = mongo_connection_handler.get_client()
        assert client is not None
        
                
    def test_context_manager(self):
        with MongoConnectionHandler() as mongo_connection_handler:
            client = mongo_connection_handler.get_client()
            assert client is not None
        client = mongo_connection_handler.get_client()
        assert client is None