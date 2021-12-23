class Product:
    """Class, which describe product"""

    def __init__(self, title, price, description=''):
        """Initialize attributes Product's instances"""
        self.title = title
        self.price = price
        self.description = description

    def __str__(self):
        return f'{self.title}: {self.price} грн'


class Customer:
    """Class, which describe customer"""

    def __init__(self, name, surname, phone):
        """Initialize attributes Customer's instances"""
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name[0]}., {self.phone}'

class Order:
    "Class, which describe order"

    def __init__(self, customer: Customer, products = None):
        self.customer = customer
        self.products = products

    def __str__(self):
        res = '\n'.join(map(str, self.products))
        return f'{self.customer}\n{res}'

    def total_price(self):
        s = 0
        for item in self.products:
            s += item.price
        return s

if __name__ == '__main__':
    x = Product('apple', 23)
    y = Product('banana', 25)
    z = Product('orange', 22)

    customer_1 = Customer('Ivan', 'Ivanov', '050689438')
    customer_2 = Customer('Petr', 'Petrov', '067892410')

    order_1 = Order(customer_1, [x, y, z])
    order_2 = Order(customer_2, [x, z])

    print(order_1)
    print(order_2)
