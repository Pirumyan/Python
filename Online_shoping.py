from abc import ABC, abstractmethod

class Customer:
    def __init__(self, name, surname, email, phone_number):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.orders = []

    def view_order_history(self):
        return self.orders

class Product(ABC):
    def __init__(self, name, price, description, reviews=None):
        self.name = name
        self.price = price
        self.description = description
        self.reviews = reviews if reviews is not None else []

    def read_reviews(self):
        return self.reviews

    def add_review(self, new_comment):
        self.reviews.append(new_comment)

    @abstractmethod
    def additional_info(self):
        pass

class Elector(Product):
    def __init__(self, name, price, description, volt, reviews=None):
        super().__init__(name, price, description, reviews)
        self.volt = volt

    def additional_info(self):
        return f"Voltage: {self.volt}"

class Clouts(Product):
    def __init__(self, name, price, description, material, reviews=None):
        super().__init__(name, price, description, reviews)
        self.material = material

    def additional_info(self):
        return f"Material: {self.material}"

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
        self.total_price = sum(product.price for product in products)
        self.customer.orders.extend([product.name for product in products])

    @staticmethod
    def search_products(keyword, product_list):
        res = ['yes' for product in product_list if keyword.lower() in product.name.lower()]
        return 'yes we have ' if len(res) > 0 else 'We dont have'

    @staticmethod
    def purchase(customer, product):
        order = Order(customer, [product])
        return order.total_price

# Example usage
customer = Customer("John", "Doe", "john.doe@email.com", "123-456-7890")
product_list = [Elector("Elector1", 50, "Electrical appliance", 220), Clouts("Clouts1", 20, "Clothing accessory", "Leather")]

search_result = Order.search_products("Elector", product_list)

print(search_result)

purchase_total = Order.purchase(customer, product_list[0])
print(f"Total Purchase Amount: {purchase_total}")
print(customer.view_order_history())