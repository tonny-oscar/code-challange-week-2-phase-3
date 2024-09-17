class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer(name={self.name}, email={self.email})"

class Coffee:
    def __init__(self, blend, size):
        self.blend = blend
        self.size = size

    def __str__(self):
        return f"Coffee(blend={self.blend}, size={self.size})"

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = float(price)

    def __str__(self):
        return f"Order(customer={self.customer}, coffee={self.coffee}, price={self.price})"

# Example usage:
customer = Customer(name="Raymond Sang", email="raymond.sang@example.com")
coffee = Coffee(blend="Espresso", size="Large")
order = Order(customer=customer, coffee=coffee, price=3.5)

print(order)