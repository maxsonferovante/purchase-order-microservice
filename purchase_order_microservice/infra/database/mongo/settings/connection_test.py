import pytest

from purchase_order_microservice.infra.database.mongo.settings.connection import MongoConnectionHandler

class TestMongoConnectionHandler:
    @pytest.mark.skip(reason="Sensive test")
    def test_instance(self):
        mongo_connection_handler = MongoConnectionHandler()
        assert isinstance(mongo_connection_handler, MongoConnectionHandler)

    @pytest.mark.skip(reason="Sensive test")        
    def test_get_client(self):
        mongo_connection_handler = MongoConnectionHandler()
        client = mongo_connection_handler.get_client()
        assert client is not None
    
    @pytest.mark.skip(reason="Sensive test")                
    def test_get_db_connection(self):
        mongo_connection_handler = MongoConnectionHandler()
        db_connection = mongo_connection_handler.get_db_connection()
        assert db_connection is not None
    @pytest.mark.skip(reason="Sensive test")                                
    def test_context_manager(self):
        with MongoConnectionHandler() as mongo_connection_handler:
            client = mongo_connection_handler.get_client()
            assert client is not None
        client = mongo_connection_handler.get_client()
        assert client is None