from customer import Customer
from coffee import Coffee

class Order:
    all_orders = []  # Class variable to track all orders

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

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def coffee(self) -> Coffee:
        return self._coffee

    @property
    def price(self) -> float:
        return self._price

    def __repr__(self) -> str:
        return (f"Order(customer={self.customer}, coffee={self.coffee}, "
                f"price={self.price})")
