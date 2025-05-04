class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
if __name__ == "__main__":
    # Create a product
    product = Product("Laptop", 1000)
    
    # Get price using property
    print(f"Current price: ${product.price}")
    
    # Set new price
    product.price = 1200
    print(f"New price: ${product.price}")
    
    # Try to set negative price
    try:
        product.price = -100
    except ValueError as e:
        print(f"Error: {e}")
    
    # Delete price
    del product.price 