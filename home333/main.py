from utils import calculate_change


def test_calculate_change():
    assert calculate_change(100, 200) == {100: 1}
    assert calculate_change(100, 150) == {50: 1}
    assert calculate_change(100.50, 200) == {100: 1, 50: 1, 0.50: 1}
    assert calculate_change(10, 5) == {}
    assert calculate_change(10, 9.99) == {0.01: 1}


def test_calculate_change_raises():
    try:
        calculate_change(100, "abc")
    except TypeError:
        pass
    else:
        raise AssertionError("TypeError not raised")

    try:
        calculate_change(100, [5000, 5000])
    except TypeError:
        pass
    else:
        raise AssertionError("TypeError not raised")

    try:
        calculate_change(100, 50)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError not raised")


if __name__ == "__main__":
    cost = float(input("Введите стоимость товара: "))
    paid = sum(map(float, input("Введите купюры/монеты: ").split()))
    change = calculate_change(cost, paid)
    print("Сдача:")
    for i, count in change.items():
        print(count, "*", i)
