
from typing import List

from pydantic.dataclasses import dataclass
from pydantic import Field, RootModel

from datetime import datetime

from .product import Product

@dataclass(slots=True, kw_only=True)
class Order:
    order_id: str = Field(init=False)
    client_id: str
    product_list: List[Product] = Field(default_factory=List[Product])
    total: float= Field(init=False, default=0.0)    
    created_at: datetime = Field(init=False, default_factory=datetime.now)
    updated_at: datetime = Field(init=False, default_factory=datetime.now)
    
    def __post_init__(self):
        self.__calculate_total()
    
    def __calculate_total(self):
        self.total = sum([product.price for product in self.product_list])
    