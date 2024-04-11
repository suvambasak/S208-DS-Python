numbers = [1, 2, 3, 4, 5]

# Calculate sum
sum = 0
for num in numbers:
    sum += num

# Calculate average
average = sum / len(numbers)

# Calculate variance
variance = 0
for num in numbers:
    variance += (num - average) ** 2
variance /= len(numbers)


print(average)
print(variance)
