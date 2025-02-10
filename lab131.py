def sum_positive_numbers(*numbers):
    results = [sum(range(num + 1)) if num > 0 else 0 for num in numbers]
    return results


# Приклад виклику функції
if __name__ == "__main__":
    test_numbers = [3, 5, -2, 0, 7]
    print(sum_positive_numbers(*test_numbers))
