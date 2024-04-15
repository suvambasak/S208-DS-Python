# Functional Programming

## What is Functional Programming?

Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. Key concepts include:

- **Pure functions:** Functions that always produce the same output for the same input, with no side effects.
- **Immutability:** Data structures, once created, cannot be modified.
- **Higher-order functions:** Functions that can take other functions as arguments or return functions as results.
- **Recursion:** A technique where a function calls itself to solve smaller instances of the same problem.

## Use of Functional Programming

Functional programming offers several benefits:

- **Simplicity:** Pure functions and immutability make code easier to understand and reason about.
- **Concurrency:** Immutability and lack of shared state make it easier to write parallel and concurrent code.
- **Modularity:** Functions can be easily composed and reused, leading to more modular and maintainable codebases.
- **Safety:** Pure functions and immutability reduce the likelihood of bugs and make it easier to test code.

## Real-World Example

Consider a scenario of processing a list of numbers to calculate statistics like sum, average, and variance.

In an imperative style (non-functional), code might look like this:

```python
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
```

This functional style, though initially complex, leads to more concise, readable, and maintainable code


```python

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
variance_result = sum(map(lambda x: x ** 2, map(subtract_mean, numbers))) / len(numbers)
```