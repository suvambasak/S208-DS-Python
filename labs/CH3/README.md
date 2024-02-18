# LAB Week 3

## Problem statement 1
Write the code for selection sort. The code should work for any input data.

Complete the `selection_sort` function in `sorting.py` file.

Input
- `data_list` : Unsorted list of integer numbers

Output
- Return None

**Examples**
| Input  | Output |
| ------------- | ------------- |
| [1,2,3]  | [1,2,3]  |
| [3,2,1] | [1,2,3]   |
| [2,3,1] | [1,2,3]   |


## Problem statement 2
Write the code for insertion sort. The code should work for any input data.

Complete the `insertion_sort` function in `sorting.py` file.

Input
- `data_list` : Unsorted list of integer numbers

Output
- Return None

**Examples**
| Input  | Output |
| ------------- | ------------- |
| [1,2,3]  | [1,2,3]  |
| [3,2,1] | [1,2,3]   |
| [2,3,1] | [1,2,3]   |


## Problem statement 3
Write the code to merge two sorted list. The code should work for any input data.

Complete the `merge` function in `sorting.py` file.

Input
- `list_1` : 1st sorted list of integer numbers
- `list_2` : 2nd sorted list of integer numbers

Output
- New sorted list of `list_1`+`list_1`

**Examples**
| Input  | Output |
| ------------- | ------------- |
| [1,3,5], [0,2,4]  | [0,1,2,3,4,5]  |
| [1], [0,2,4] | [0,1,2,4]   |


## Problem statement 4
Write the code for merge sort. The code should work for any input data.

Complete the `merge_sort` function in `sorting.py` file using the above `merge` function.


Input
- `data_list` : Unsorted list of integer numbers
- `lindex` : Left index of the list (starting index)
- `rindex` : Right index of the list (ending index)

Output
- Sorted `data_list`

**Examples**
| Input  | Output |
| ------------- | ------------- |
| [9,8,7,6,5,4,3,2,1], 0, 8  | [1,2,3,4,5,6,7,8,9]  |


## Problem statement 5
Write the code to partition a list. The code should work for any input data.

Complete the `partition` function in `sorting.py` file.

Input
- `data_list` : Unsorted list of integer numbers
- `lindex` : Left index of the list (starting index)
- `rindex` : Right index of the list (ending index)

Output
- Return int value which is index of pivot element.

**Examples**
| Input  | Output |
| ------------- | ------------- |
| [5,7,3,2,6,9,3,2], 0, 8 | 4 |

## Problem statement 6
Write the code for quick sort. The code should work for any input data.

Complete the `quick_sort` function in `sorting.py` file using the above `partition` function.

Input
- `data_list` : Unsorted list of integer numbers
- `lindex` : Left index of the list (starting index)
- `rindex` : Right index of the list (ending index)

Output
- Return None

**Examples**
| Input  | Output |
| ------------- | ------------- |
| [9,8,7,6,5,4,3,2,1], 0, 8  | [1,2,3,4,5,6,7,8,9]  |


## Test your code
Execute following command to test your code
```bash
python3 -m unittest -v test_sorting.py
```