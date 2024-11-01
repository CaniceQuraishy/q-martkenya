class Product:
    def __init__(self, name, price, category, stock_quantity):
        self.name = name
        self.price = price
        self.category = category
        self._stock_quantity = stock_quantity  # Private attribute

    def apply_discount(self, discount_percentage):
        """Apply a discount to the product."""
        discount_amount = (discount_percentage / 100) * self.price
        return self.price - discount_amount

    def update_stock(self, quantity):
        """Update the stock after a purchase."""
        if quantity <= self._stock_quantity:
            self._stock_quantity -= quantity
        else:
            raise ValueError("Not enough stock available.")

    def __str__(self):
        return f"{self.name} ({self.category}): Ksh {self.price:.2f}, Stock: {self._stock_quantity}"
