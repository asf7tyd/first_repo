n = int(input("Введите количество элементов: "))
x = []
for i in range(1, n + 1):
    x += [i] * i
print(x[:n])
