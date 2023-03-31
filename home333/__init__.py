DENOMINATIONS = {5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01}


def calculate_change(cost, paid):
    change = paid - cost
    result = {}
    for i in sorted(DENOMINATIONS, reverse=True):
        count = int(change // i)
        if count > 0:
            result[i] = count
            change -= count * i
    return result


if __name__ == "__main__":
    cost = float(input("Введите стоимость товара: "))
    paid = sum(map(float, input("Введите купюры/монеты: ").split()))
    change = calculate_change(cost, paid)
    print("Сдача:")
    for i, count in change.items():
        print(count, "*", i)
