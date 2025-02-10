def sum_positive_numbers(*numbers):
    results = []
    for num in numbers:
        if num > 0:
            total = sum(i for i in range(num + 1))
            results.append(total)
        else:
            results.append(0)
    return results


# Приклад виклику функції
if __name__ == "__main__":
    test_numbers = [3, 5, -2, 0, 7]
    print(sum_positive_numbers(*test_numbers))
