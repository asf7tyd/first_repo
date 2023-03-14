# numbers = [2, 3, 4, 5, 7, 6]
# for i in numbers:
#  x = i ** 2
#  print(x)
from itertools import zip_longest

cars = (input("Введите список машин: "))
names = (input("Введите список имен: "))

names = names.split(',')
cars = cars.split(',')

names = sorted(names)
cars = sorted(cars)

if len(cars) == len(names):
    result = list(zip(names, cars))
    print(result)

elif len(cars) != len(names):
    print("Кому-то не достанется автомобиля!")
