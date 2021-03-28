class AbstractCat:
    def __init__(self):
        self.ves = 0
        self.remains = 0

    def eat(self, food):
        b = 0
        food += self.remains
        while food > 10:
            if food > 10:
                food -= 10
                b += 1
        self.remains = food
        self.ves += b
        return 'AbstractCat ({})'.format(self.ves)


class Kitten(AbstractCat):
    def __init__(self, nummber):
        self.nummber = nummber
        super().__init__()

    def meow(self):
        return 'meow...'

    def sleep(self):
        b = ''
        while self.nummber > 5:
            b += 'Snore'
            self.nummber -= 5
        return b


class Cat(Kitten):
    def __init__(self, nummber, name):
        super().__init__(nummber)
        self.name = name

    def meow(self):
        return 'MEOW...'

    def get_name(self):
        return self.name

    def catch_mice(self):
        return 'Got it!'


# abscat = AbstractCat()
# abscat.eat(125)
# abscat.eat(17)
# abscat = abscat.eat(0)
# print(abscat)
# kit = Kitten(21)
# print(kit.sleep())
# cat = Cat(83, 'Molly')
# print(cat.meow())
# print(cat.get_name())

kit = Kitten(15)
kit.eat(24)
print(kit)
cat = Cat(41, 'Molly')
print(cat.catch_mice())
print(cat)