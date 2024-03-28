# LAB Week 7

## Problem statement 1
Complete the function `insert` in `binary_tree.py` to construct a unique binary tree.

## Problem statement 2
Complete the function `in_order` in `binary_tree.py` to implement in order travarsal of a binary tree.

## Problem statement 3
Complete the function `pre_order` in `binary_tree.py` to implement pre order travarsal of a binary tree.

## Problem statement 4
Complete the function `post_order` in `binary_tree.py` to implement post order travarsal of a binary tree.

## Test your code
No test case is given as of now. You could execute and verify the correctness of your code. Try to test you code kind of all possible input combinations. Some of the input and output are given below for testing your code.

### CASE I

Insert sequence:

```python
root = insert(root, 33)
root = insert(root, 40)
root = insert(root, 30)
root = insert(root, 10)
root = insert(root, 15)
root = insert(root, 50)
root = insert(root, 37)
```

Output:
- Pre order: 33 30 10 15 40 37 50
- In order: 10 15 30 33 37 40 50 
- Post order: 15 10 30 37 50 40 33


### CASE II

Insert sequence:

```python
root = insert(root, 5)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 9)
root = insert(root, 8)
```

Output:

- Pre order: 5 1 6 7 10 9 8 
- In order: 1 5 6 7 8 9 10
- Post order: 1 8 9 10 7 6 5
