from pydantic.dataclasses import dataclass
from pydantic import Field, RootModel

from datetime import datetime


@dataclass
# Product colocado na ordem de compra, sugira um nome melhor
class Product:
    product_id: str
    name: str
    price: float            
    created_at: datetime = Field(init=False, default_factory=datetime.now)
    updated_at: datetime = Field(init=False, default_factory=datetime.now)