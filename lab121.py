import doctest


def calculate_sum(N):
    """
    Обчислює суму чисел від 1 до N за допомогою sum() та range().

    >>> calculate_sum(5)
    15
    >>> calculate_sum(10)
    55
    >>> calculate_sum(1)
    1
    >>> calculate_sum(0)
    Traceback (most recent call last):
    ValueError: Число має бути більше 0
    >>> calculate_sum(-5)
    Traceback (most recent call last):
    ValueError: Число має бути більше 0
    """
    if N < 1:
        raise ValueError("Число має бути більше 0")
    return sum(i for i in range(1, N + 1))


if __name__ == "__main__":
    try:
        # Запитуємо у користувача число
        N = int(input("Введіть число N: "))

        # Обчислюємо суму та виводимо результат
        summa = calculate_sum(N)
        print(f"Сума чисел від 1 до {N} дорівнює {summa}")

    except ValueError as e:
        print(f"Помилка: {e}. Введіть коректне додатне число.")

    # Запуск doctest
    doctest.testmod()
