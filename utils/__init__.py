def calculate_change(price: float, payment: List[float]) -> List[float]:
    denominations = {5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01}
    total_payment = sum(payment)
    if total_payment < price:
        raise ValueError("Insufficient payment.")
    change = total_payment - price
    change_denominations = []
    for denomination in sorted(denominations, reverse=True):
        while change >= denomination:
            change_denominations.append(denomination)
            change -= denomination
    return change_denominations


if __name__ == "__main__":
    price = float(input("Введите стоимость товара: "))
    payment = [float(x) for x in input("Введите купюры/монеты через пробел: ").split()]
    try:
        change = calculate_change(price, payment)
        print("Сдача:", ", ".join(str(x) for x in change))
    except ValueError as e:
        print("Ошибка:", e)
