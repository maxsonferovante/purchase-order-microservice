from purchase_order_microservice.domain.use_cases.order_register_interface import OrderRegisterInterface
from purchase_order_microservice.data.interfaces.order_repository_interface import OrderRepositoryInterface
from purchase_order_microservice.domain.models.order import Order

class OrderRegisterUseCase(OrderRegisterInterface):
    def __init__(self, repository: OrderRepositoryInterface):
        self.repository = repository

    def register(self, order: Order) -> Order:
             
        order_result = self.__register_order(order)
        
        return self.__format_response(order_result)    
    
    @staticmethod
    def __register_order(order: Order):
        return self.repository.create_order(order)
    
    @staticmethod
    def __format_response(order: Order):
        response = {
            'type': 'Orders',
            'count': 1,
            'atributes': order.to_dict()
        }
        