from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for current_product in self.products:
            if current_product.name == product_name:
                return current_product

    def remove(self, product_name):
        current_product = self.find(product_name)
        if current_product is not None:
            self.products.remove(current_product)

    def __repr__(self):
        result = ''
        for product in self.products:
            result += f"{product.name}: {product.quantity}\n"

        return result.strip()