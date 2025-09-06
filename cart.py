"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""

class ShoppingCart:
    def __init__(self, prices):
        self.items = {}
        self.prices = prices

    def add_item(self, item, quantity):
        if quantity <= 0:
            return "Quantity must be greater than Zero"
        
        else:
            if item in self.items:
                self.items[item] += quantity
                return self.items

            elif item in self.prices:
                self.items.update({item:quantity})
                return self.items

            else:
                return "Item does not Exist!"

    def calculate_total(self):
        for key, value in self.items.items():
            for key, value in self.prices.items():
                return f"Item: {key}, Quantity: {self.items[key]}, Amount: {self.items[key] * value}"

    def remove_item(self, item, quantity):
        if item in self.items:
            self.items[item] -= quantity
        return self.items

prices = {"shirt": 5000, "shoes": 12000}
cart = ShoppingCart(prices)
print(cart.add_item("shirt", 0))
print(cart.add_item("shirt", 5))
print(cart.add_item("shirt", 5))
print(cart.add_item("shoes", 5))
print(cart.calculate_total())
print(cart.remove_item("shirt", 10))
print(cart.calculate_total())

print()


