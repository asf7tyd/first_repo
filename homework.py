# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# max_number = max(numbers)
# min_number = min(numbers)

# print("Максимальное число:", max_number)
# print("Минимальное число:", min_number)
# for num in numbers:
#  if num % 3 == 0 and num % 5 != 0:
#     print(num)
n = [1, 2, 3, 4, 5, 2, 3, 4, 5]
for num in n:
    if n.count(num) == 1:
        print(num)
        break
