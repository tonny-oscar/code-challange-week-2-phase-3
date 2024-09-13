from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

def test_coffee_shop_system():
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")

    # Create coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    # Create orders
    order1 = alice.create_order(espresso, 2.5)
    order2 = bob.create_order(espresso, 3.0)
    order3 = alice.create_order(latte, 4.0)

    # Print details
    print("All Orders:", Order.all_orders)
    print("Alice's Orders:", alice.orders())
    print("Bob's Orders:", bob.orders())
    print("Espresso Orders:", espresso.orders())
    print("Latte Orders:", latte.orders())
    print("Alice's Coffees:", alice.coffees())
    print("Espresso Customers:", espresso.customers())
    print("Number of Orders for Espresso:", espresso.num_orders())
    print("Average Price for Espresso:", espresso.average_price())

if __name__ == "__main__":
    test_coffee_shop_system()
