from typing import List, Union

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

    def create_order(self, coffee: 'Coffee', price: float) -> 'Order':
        return Order(self, coffee, price)

    def orders(self) -> List['Order']:
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self) -> List['Coffee']:
        return list(set(order.coffee for order in self.orders()))

class Coffee:
    all_orders = []  # This will store all the orders for aggregate functions

    def __init__(self, name: str):
        self._name = None
        self.name = name  # Use the property setter for validation

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        if hasattr(self, '_name'):  # If name is already set, it shouldn't change
            raise AttributeError("Coffee name cannot be changed after initialization")
        self._name = value

    def orders(self) -> List['Order']:
        return [order for order in Coffee.all_orders if order.coffee == self]

    def customers(self) -> List['Customer']:
        return list(set(order.customer for order in self.orders()))

    def num_orders(self) -> int:
        return len(self.orders())

    def average_price(self) -> float:
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(order.price for order in orders) / len(orders)

class Order:
    all_orders = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)
        Coffee.all_orders.append(self)

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def coffee(self) -> Coffee:
        return self._coffee

    @property
    def price(self) -> float:
        return self._price
        
print(Order.all_orders)
