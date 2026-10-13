'''Product class
Create a Product class with the product name, price, and quantity. 
Add an instance method to calculate the total cost. 
Take these values from the user and display the product name and total cost.'''


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price*self.quantity


product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
product_quantity = int(input("Enter product quantity: "))
product = Product(product_name, product_price, product_quantity)
print("Product Name: ", product.name)
print("Total Cost: ", product.total_cost())
