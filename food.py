class Food:
    count = 0

    def __init__(self, name, taste, price, amount):
        self.name = name
        self.__price = price
        self.taste = taste
        self.__class__.count += 1
        self.amount = amount
        self.__class__.count += self.amount

    def __str__(self):
        return f'{self.name} ({self.taste}, {self.__price} руб, {self.amount} на складе)'

    def __eq__(self, other):
        return type(other) == Food and self.name == other.name and self.taste == other.taste

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} food items'

    def consume(self):
        if self.amount > 0:
            print(f'{self.name} was eaten')
            self.amount -= 1
            self.__class__.count -= 1
        else:
            print(f'we have no {self.name}')

    def __iadd__(self, other):
        if type(other) == int:
            self.amount += other
            self.count += other
        return self

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if 10 <= new_price <= 20000:
            self.__price = new_price
#---------------------------------------------------------------------------------------

class Drink:
    count = 0

    def __init__(self, name, drink_type, price):
        self.name = name
        self.type = drink_type
        self.price = price
        self.__class__.count += 1

    def __str__(self):
        return f'{self.type} "{self.name}" ({self.price})'

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} drinks'

    def consume(self):
        print(f'{self.name} was drunk')
#------------------------------------------------------------------------------------------

cake_1 = Food('Торт', 'вкусный', 120, 5)
cake_2 = Food('Торт', 'вкусный', 213, 4)
cake_1.name = 'Тортик'
print(cake_1 == cake_2)
sushi = Food('Суши', 'вегетарианские', 390, 12)
print(sushi)
sushi += 1
print(sushi)
sushi.consume()
print(sushi)

print(Food.get_report())

print(sushi == 5)
a = 0

#-------------------------------------------------

latte = Drink('Латте', 'Кофе', 220)
print(latte)
kvass = Drink('Натуральный', 'Квас', 150)
print(kvass)