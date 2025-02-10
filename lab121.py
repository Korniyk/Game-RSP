# Додаток для обчислення суми чисел від 1 до N з використанням sum(), for і try...except


def calculate_sum(N):
    """Обчислює суму чисел від 1 до N за допомогою sum() та range()."""
    return sum(i for i in range(1, N + 1))


try:
    # Запитуємо у користувача число
    N = int(input("Введіть число N: "))

    # Перевіряємо, щоб число було додатним
    if N < 1:
        raise ValueError("Число має бути більше 0")

    # Обчислюємо суму та виводимо результат
    summa = calculate_sum(N)
    print(f"Сума чисел від 1 до {N} дорівнює {summa}")

except ValueError as e:
    print(f"Помилка: {e}. Введіть коректне додатне число.")
