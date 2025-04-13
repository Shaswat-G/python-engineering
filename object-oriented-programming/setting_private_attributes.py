class Product:
    
    def __init__(self, price):
        self.set_price(price)  # Using the setter method to set the price
        
        
    def set_price(self, price):
        if price <0:
            raise ValueError("Price cannot be negative")
        else:
            self.__price = price
        
        
    def get_price(self):
        return self.__price
    
    
product = Product(20)
print(product.get_price())  # Output: 20
        