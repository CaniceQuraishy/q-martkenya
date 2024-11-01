from product import Product
from cart import Cart
from store import Store

def main():
    store = Store()

    # Add some products to the store
    store.add_product(Product("Smartphone", 30000, "Electronics", 10))
    store.add_product(Product("T-shirt", 1500, "Clothing", 20))
    store.add_product(Product("Laptop", 60000, "Electronics", 5))

    cart = Cart()  # Initialize cart outside the loop for persistence

    while True:
        print("\nQ-mark Kenya:")
        store.display_products()

        while True:
            product_index = input("\nEnter the product number to add to the cart (or 'done' to finish): ")
            if product_index.lower() == 'done':
                break
            
            if product_index.isdigit():
                product_index = int(product_index)
                if 1 <= product_index <= len(store.inventory):
                    product = store.inventory[product_index - 1]
                    quantity = int(input(f"Enter the quantity for {product.name}: "))
                    try:
                        cart.add_product(product, quantity)
                    except ValueError as e:
                        print(e)
                else:
                    print("Invalid index. Please try again.")
            else:
                print("Invalid input. Please enter a number.")

        # View cart and checkout
        print("\nYour Cart:")
        cart.view_cart()  # This already prints the total cost.

        if cart.total_cost > 0:
            # Ask if the user wants to remove items from the cart
            while True:
                remove_items = input("Do you want to remove any items from your cart? (yes/no): ")
                if remove_items.lower() == 'yes':
                    if cart.products:  # Check if there are items in the cart
                        print("\nItems in your cart:")
                        cart.view_cart()
                        remove_index = input("Enter the product number to remove from the cart (or '0' to skip): ")
                        if remove_index.isdigit():
                            remove_index = int(remove_index)
                            if remove_index == 0:
                                print("Skipping removal.")
                            elif 1 <= remove_index <= len(cart.products):
                                product_to_remove = cart.products[remove_index - 1][0]  # Get the product object
                                quantity_to_remove = int(input(f"Enter the quantity of {product_to_remove.name} to remove: "))
                                try:
                                    cart.remove_product(product_to_remove, quantity_to_remove)
                                    cart.view_cart()  # Show updated cart after removal
                                except ValueError as e:
                                    print(e)
                            else:
                                print("Invalid index. Please try again.")
                        else:
                            print("Invalid input. Please enter a number.")
                    else:
                        print("Your cart is empty. No items to remove.")
                elif remove_items.lower() == 'no':
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            # Proceed to payment
            payment = float(input("Enter the amount you are paying: Ksh "))

            if payment >= cart.total_cost:  # Use cart.total_cost directly
                change = payment - cart.total_cost
                print(f"Thank you for your purchase! Your change is: Ksh {change:.2f}")
                cart.checkout()  # Clear the cart after checkout
            else:
                print("Insufficient payment. Please try again.")
        else:
            print("Your cart is empty. No checkout process.")

        # Ask if user wants to continue shopping
        continue_shopping = input("\nDo you want to continue shopping? (yes/no): ")
        if continue_shopping.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
