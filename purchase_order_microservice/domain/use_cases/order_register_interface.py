from abc import ABC, abstractmethod
from purchase_order_microservice.domain.models.order import Order


class OrderRegisterInterface(ABC):
    @abstractmethod
    def register(self, order: Order) -> Order:
        pass