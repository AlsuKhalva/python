class Product:
    def __init__(self, name, price, discount=0, stock=0, max_discount=20.0):
        self.name = name.strip()
        if not len(self.name) >= 2:
            raise ValueError('Слишком короткое название товара')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('Слишком большая скидка')
        if self.discount > self.max_discount:
            self.discount = self.max_discount


    def discounted(self):
        return self.price - self.price * self.discount / 100


    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        self.stock -= items_count


    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>'

    product1 = Product('Товар', 100,, stock=10)
    product1.sell(5)
    print(product1)