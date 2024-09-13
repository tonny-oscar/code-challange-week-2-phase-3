from typing import List
from coffee import Coffee
from order import Order

class Customer:
    def __init__(self, name: str):
        self._name = None
        self.name = name  # Use the property setter for validation

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = value

    def create_order(self, coffee: Coffee, price: float) -> 'Order':
        return Order(self, coffee, price)

    def orders(self) -> List['Order']:
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self) -> List['Coffee']:
        return list(set(order.coffee for order in self.orders()))

    def __repr__(self) -> str:
        return f"Customer(name='{self.name}')"