# LAB Week 2

## Problem statement 1
Write the code for Linear search. The code should work for any input data.

Complete the `linear_search` function in `searching.py` file.

Input
- `data_list` : List of integer number
- `key`: Integer number

Output
- Returns a tuple of bool and index 
- If the `key` element not found in `data_list` return False status and index at -1
- If the `key` element found in `data_list` return True status and index of the `key` in `data_list`

**Examples**
| Input  | Output |
| ------------- | ------------- |
| [1,2,3], 3  | (True, 2)  |
| [1,2,3], 5 | (False, -1)  |


## Problem statement 2
Write the code for **iterative** Binary search. The code should work for any input data.

Complete the `binary_search` function in `searching.py` file.


Input
- `data_list` : List of integer number
- `key`: Integer number
- `left`: Left index of the list (start index)
- `right`: Right index of the list (end index)

Output
- Returns a tuple of bool and index 
- If the `key` element not found in `data_list` return False status and index at -1
- If the `key` element found in `data_list` return True status and index of the `key` in `data_list`

**Examples**
| Input  | Output |
| ------------- | ------------- |
| [1,2,3], 3  | (True, 2)  |
| [1,2,3], 5 | (False, -1)  |


## Problem statement 3
Write the code for **recursive** Binary search. The code should work for any input data.

Complete the `binary_recursive_search` function in `searching.py` file.


Input
- `data_list` : List of integer number
- `key`: Integer number
- `left`: Left index of the list (start index)
- `right`: Right index of the list (end index)

Output
- Returns a tuple of bool and index 
- If the `key` element not found in `data_list` return False status and index at -1
- If the `key` element found in `data_list` return True status and index of the `key` in `data_list`

**Examples**
| Input  | Output |
| ------------- | ------------- |
| [1,2,3], 3  | (True, 2)  |
| [1,2,3], 5 | (False, -1)  |



## Test your code
Execute following command to test your code
```bash
python3 -m unittest -v test_searching.py
```