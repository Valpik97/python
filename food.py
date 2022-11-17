class item:
    count = 0

    def __init__(self, name, price, amount=1):
        self.name = name
        self._amount = amount
        self.price = price
        self.__class__.count += amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        if new_amount > 0:
            self.__class__.count = new_amount - self._amount
            self._amount = new_amount

    def __str__(self):
        return f'{self.name} ({self.price}), {self.amount} на складе'


class Food(item):

    def __init__(self, name, taste, price, amount=1):
        super().__init__(name, price, amount)
        self.taste = taste
        self._amount = amount
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
            self._amount -= 1
            self.__class__.count -= 1
        else:
            print(f'we have no {self.name}')

    def __iadd__(self, other):
        if type(other) == int:
            self._amount += other
            self.__class__.count += other
        return self

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if 10 <= new_price <= 20000:
            self.__price = new_price
#---------------------------------------------------------------------------------------

class Drink(item):

    def __init__(self, name, drink_type, price, amount=1):
        super().__init__(name, price, amount)
        self.type = drink_type

    def __str__(self):
        return f'{self.type} "{self.name}" ({self.price}), {self.amount} на складе'

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} drinks'

    def consume(self):
        if self.amount > 0:
            print(f'{self.name} was drunk')
            self._amount -= 1
            self.__class__.count -= 1
        else:
            print(f'we have no {self.name}')
#------------------------------------------------------------------------------------------

cake_1 = Food('Торт', 'вкусный', 120, 5)
cake_2 = Food('Торт', 'вкусный', 213, 4)
latte = Drink('Латте', 'Кофе', 220, 2)
kvass = Drink('Натуральный', 'Квас', 150, 4)
sushi = Food('Суши', 'вегетарианские', 390, 12)
cake_1.name = 'Тортик'
dual_sense = item('DualSense 5', 7000)

#------------------------------------------------------------------------------------------

for item in cake_1, cake_2, sushi, latte, kvass, dual_sense:
     #item.consume()
    print(item)

# print(cake_1 == cake_2)
# print(sushi)
# sushi += 1
# print(sushi)
# sushi.consume()
# print(sushi)
# print(Food.get_report())
# print(sushi == 5)
# print(Drink.count)
