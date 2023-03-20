class Car:
    year = 2023
    def __init__ (self, model: str = 'Lada', color: str = 'white', volume: float = 8.0):
        self.model = 'Введите модель'
        self.color = color
        self.volume = volume
        # if model == 'X5':
        #     self.horse_power = volume
        # else:
        #     self.volume = volume

    def gas(self):
        print('Бррррррбрррр!')

    def present(self):
        return f'{self.__ne__}'

    def __str__ (self):
        return f'Это машина {self.model}, {self.color} цвета и объем {self.volume}'


ferrari = Car('F355', 'red', 6.0)
bmw = Car('X5', 'black', 5.0)
# print(ferrari.model)
# print(bmw.color)
#
# bmw.color = 'green'
# print(bmw.color)
#
# ferrari.sport = True
#
# print(ferrari.sport)
# print(bmw.sport)

# ferrari.gas()
# print(ferrari.present())
# print(bmw.year)
#
# bmw.year = 1986
# print(bmw.year)
# print(ferrari.year)
print(ferrari)




















