# №1
words = input("Введите слова через запятую: ").split(",")
words = [word.strip() for word in words]
words.sort()
print("Отсортированные слова: ", ", ".join(words))
