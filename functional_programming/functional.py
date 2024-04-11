from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Define pure functions for calculations


def add(x, y):
    return x + y


def subtract_mean(x):
    return x - sum(numbers) / len(numbers)


# Calculate sum
sum_result = reduce(add, numbers)

# Calculate average
average_result = sum(numbers) / len(numbers)

# Calculate variance
variance_result = sum(
    map(lambda x: x ** 2, map(subtract_mean, numbers))) / len(numbers)

print(average_result)
print(variance_result)
