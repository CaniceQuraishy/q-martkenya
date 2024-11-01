from product import Product

class Cart:
    def __init__(self):
        self.products = []
        self.total_cost = 0.0

    def add_product(self, product: Product, quantity: int):
        """Add a product to the cart if available."""
        if product._stock_quantity >= quantity:
            self.products.append((product, quantity))
            self.total_cost += product.price * quantity
            product.update_stock(quantity)
        else:
            raise ValueError(f"Not enough stock for {product.name}.")

    def remove_product(self, product: Product, quantity: int):
        """Remove a specified quantity of a product from the cart."""
        for index, item in enumerate(self.products):
            if item[0].name == product.name:
                if quantity >= item[1]:
                    self.total_cost -= item[0].price * item[1]
                    del self.products[index]  # Remove the entire item
                    print(f"All {item[1]} of {product.name} have been removed from your cart.")
                else:
                    new_quantity = item[1] - quantity
                    self.products[index] = (item[0], new_quantity)  # Update with new quantity
                    self.total_cost -= item[0].price * quantity
                    print(f"{quantity} of {product.name} has been removed from your cart.")
                return  # Exit the method after removing the item
        raise ValueError(f"{product.name} not found in cart.")

    def view_cart(self):
        """Display the items in the cart."""
        if not self.products:
            print("Your cart is empty.")
            return
        print("Items in your cart:")
        for idx, (product, quantity) in enumerate(self.products, start=1):
            print(f"{idx}. {product.name}: {quantity} x Ksh {product.price:.2f}")
        print(f"Total Cost: Ksh {self.total_cost:.2f}")  # Display total cost once

    def checkout(self):
        """Finalize the cart."""
        print("Checking out...")
        print(f"Total Cost: Ksh {self.total_cost:.2f}")
        self.products.clear()  # Clear cart after checkout
        self.total_cost = 0.0
