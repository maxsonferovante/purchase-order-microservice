from typing import List
from abc import ABC, abstractmethod
from purchase_order_microservice.domain.models.order import Order

class OrderRepositoryInterface(ABC):
    @abstractmethod
    def create_order(self, order: Order) -> Order:
        raise NotImplementedError
    
    @abstractmethod
    def get_order(self, order_id: str) -> Order:
        raise NotImplementedError
    
    @abstractmethod
    def update_order(self, order: Order) -> Order:
        raise NotImplementedError
    
    @abstractmethod
    def delete_order(self, order_id: str) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def list_orders(self) -> List[Order]:
        raise NotImplementedError
    
    