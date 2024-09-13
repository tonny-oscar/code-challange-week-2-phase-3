from typing import List
from order import Order
from customer import Customer

class Coffee:
    def __init__(self, name: str):
        self._name = None
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
            #to prevent changes after initialization
        if hasattr(self, '_name') and self._name is not None: 
            raise AttributeError("Coffee name cannot be changed after initialization")
        self._name = value

    def orders(self) -> List['Order']:
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self) -> List['Customer']:
        return list(set(order.customer for order in self.orders()))

    def num_orders(self) -> int:
        return len(self.orders())

    def average_price(self) -> float:
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(order.price for order in orders) / len(orders)

    def __repr__(self) -> str:
        return f"Coffee(name='{self.name}')"
        