from pprint import pprint

class Products:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        for product in products:
            if product.name not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(product.__str__() + '\n')
                file.close()

            else:
                print(f'Продукт {product.name}, {product.weight}, {product.category} уже есть в магазине')

s1 = Shop()
p1 = Products('Potato', 50.5, 'Vegetables')
p2 = Products('Spaghetti', 3.4, 'Groceries')
p3 = Products('Potato', 5.5, 'Vegetables')

print(p2)  #__str__

s1.add(p1, p2, p3)

print(s1.get_products())





