from product import Product

class Store:
    def __init__(self):
        self.inventory = []

    def add_product(self, product: Product):
        """Add a product to the store's inventory."""
        self.inventory.append(product)

    def display_products(self):
        """Show all available products with indices."""
        print("Available Products:")
        for index, product in enumerate(self.inventory, start=1):
            print(f"{index}. {product}")

    def search_product(self, name):
        """Search for a product by name."""
        for product in self.inventory:
            if product.name.lower() == name.lower():
                return product
        return None
