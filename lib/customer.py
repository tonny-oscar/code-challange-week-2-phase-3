class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (1 <= len(new_name) <= 15):
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        self._name = new_name

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        customer_spending = {}
        for order in coffee.orders():
            customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price
        return max(customer_spending, key=customer_spending.get)
    
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders
    

    # Create some coffee types
mocha = Coffee("Mocha")
latte = Coffee("Latte")

# Create customers
brian = Customer("Brian")
kevin = Customer("Kevin")

# Customers place orders
brian.create_order(mocha, 4.5)
brian.create_order(latte, 4.0)
kevin.create_order(mocha, 3.0)
kevin.create_order(mocha, 3.0)

# Check Brian's orders
print(f"Brian's orders: {[order.coffee.name for order in brian.orders()]}")
# Output: Brian's orders: ['Mocha', 'Latte']

# Check unique coffees Brian has ordered
print(f"Brian's unique coffees: {brian.coffees()}")
# Output unique coffees: ['Mocha', 'Latte']

# Determine who is the most aficionado of Mocha
most_aficionado = Customer.most_aficionado(mocha)
print(f"The most aficionado of Mocha is: {most_aficionado.name}")