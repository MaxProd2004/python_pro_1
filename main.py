# Задание 1
print("Задание 1")
class Product_description:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
    def __str__(self):
        return "Product [price = {}, description = {}, dimensions = {}]".format(self.price, self.description, self.dimensions)

product_1 = Product_description(1000, "This is computer", 5)
product_2 = Product_description(2500, "This is fridge", 100)
print(product_1)
print(product_2, '\n')

# Задание 2
print("Задание 2")
class Customer:
    def __init__(self, name, surname, patronymic, phone_number):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone_number = phone_number
    def __str__(self):
        return "Info about customer: [name = {}, surname = {}, patronymic = {}, phone_number = {}]".format(self.name, self.surname, self.patronymic, self.phone_number)
customer_1 = Customer("Ivan", "Ivanov", "Vasilievich", "+380965761204")
print(customer_1, '\n')

