# №№1
# numbers = input("Введите числа через пробел")
# numbers_list = numbers.split()
# numbers_list.reverse()
# print(numbers_list)
# №2
months = {1: ('Январь', 31),
          2: ('Февраль', 28),
          3: ('Март', 31),
          4: ('Апрель', 30),
          5: ('Май', 31),
          6: ('Июнь', 30),
          7: ('Июль', 31),
          8: ('Август', 31),
          9: ('Сентябрь', 30),
          10: ('Октябрь', 31),
          11: ('Ноябрь', 30),
          12: ('Декабрь', 31)

          }

month_number = int(input("Введите номер месяца: "))
if month_number in months:
    month_name, days_count = months[month_number]
    print(f"В месяце {month_name} {days_count} дней.")
else:
    print("Некорректный номер месяца.")
