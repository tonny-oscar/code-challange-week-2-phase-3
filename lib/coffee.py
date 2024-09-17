class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string of at least 3 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def add_order(self, order):
        self._orders.append(order)

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)


class Order:
    def __init__(self, customer, price):
        if not isinstance(customer, str) or len(customer) < 1:
            raise ValueError("Customer name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        
        self.customer = customer
        self.price = price


def test_coffee_class():
    coffee = Coffee("Espresso")

    order1 = Order("Kevin", 3.50)
    order2 = Order("Bob", 4.00)
    order3 = Order("Kevin", 3.75)

    coffee.add_order(order1)
    coffee.add_order(order2)
    coffee.add_order(order3)

    # Test the number of orders
    assert coffee.num_orders() == 3, "Expected 3 orders"

    # Test the customers list (unique customers)
    assert set(coffee.customers()) == {"Kevin", "Bob"}, "Expected customers are Kevin and Bob"

    # Test the average price calculation
    assert abs(coffee.average_price() - 3.75) < 1e-9, "Expected average price is 3.75"

    # Test the Coffee name
    assert coffee.name == "Espresso", "Expected coffee name is Espresso"

    # Print results
    print("All tests passed!")

# Run the test function
test_coffee_class()