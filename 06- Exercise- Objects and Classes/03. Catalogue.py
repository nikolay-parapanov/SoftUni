class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        result = list(s for s in Catalogue.products if s.startswith(first_letter))
        return result

    def __repr__(self):
        output1 = f"Items in the {self.name} catalogue:\n"
        output2 = "\n".join(sorted(Catalogue.products))
        return output1 + output2
