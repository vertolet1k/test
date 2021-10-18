class Grab:
    def grab(self, money):
        self.money = money
        return 0


class BankAccaunt(Grab):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def back(self):
        return self.money

    @back.setter
    def back(self, x):
        try:
            self.money += x
            print(f'{self.name} - {self.money}')
        except TypeError:
            print('ЛОХ')

    @back.deleter
    def back(self):
        self.money = 0
        print(f'у вас больше нет денег)) - {self.money}')

    def year(self, y):
        try:
            self.money += 0.01 * int(y.replace('%', '')) * self.money
            print(f'у вас на счету - {self.money}')
        except ValueError:
            print('ЛОШАРА')


ilya = BankAccaunt('Gay', 3)
ilya.back = 3
print(ilya.back)
del ilya.back
print(ilya.back)
# class Vika:
#     def __init__(self, stroka):
#         self.stroka = stroka

#     def umnog(self, x):
#       if isinstance(x, int):
#           return self.stroka * x

# try:
#   return self.stroka * int(x)
# except Exception as ex:
#   print(ex)
#   return self.stroka * 1

# vika = Vika('абвгде')
# print(vika.umnog('a'))

# class Plane:
#     def life(self):
#         print('fly')


# class Car:
#     def life(self):
#         print('drive')


# class Human:
#     def life(self):
#         print('life')

#     def __srat(self):
#         print('srat')


# person = Human()
# person.life()
# person.__srat()
