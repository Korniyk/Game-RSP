def sum_positive_numbers(*numbers):
    results = []
    for num in numbers:
        try:
            if num > 0:
                results.append(sum(range(num + 1)))
            else:
                results.append(0)
        except TypeError:
            results.append("Error: Invalid input")
    return results


# Приклад виклику функції
if __name__ == "__main__":
    test_numbers = [3, 5, -2, 0, 7, "text"]
    print(sum_positive_numbers(*test_numbers))
