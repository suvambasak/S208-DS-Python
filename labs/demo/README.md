# LAB Demo

## Problem statement
Complete the recursive fuction in `factorial.py`


Input
- `n` : Any integer number

Output
- Factorial of input `n` for $n >= 0$
- `None` for $n < 0$



### Template
- Given template
```Python
def fact(n: int) -> int:
    pass # Your code here (delete pass)
```
- Your code
```Python
def fact(n: int) -> int:
    if n<0:
        return None
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
```

## Test your code
Execute following command to test your code
```bash
python3 -m unittest -v test_factorial.py
```

### Correct implementation
All the test cases passed and `OK` status
```bash
test_edge_case (test_factorial.TestLossModel.test_edge_case)
Testing edge cases ... ok
test_invalid_inputs (test_factorial.TestLossModel.test_invalid_inputs)
Testing with invalid inputs (-ve numbers) ... ok
test_results (test_factorial.TestLossModel.test_results)
Testing for correct results ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.094s

OK
```

### Incorrect implementation
One test case failed hence `FAILED` status
- For -ve input `n` test failed
```bash
test_edge_case (test_factorial.TestLossModel.test_edge_case)
Testing edge cases ... ok
test_invalid_inputs (test_factorial.TestLossModel.test_invalid_inputs)
Testing with invalid inputs (-ve numbers) ... FAIL
test_results (test_factorial.TestLossModel.test_results)
Testing for correct results ... ok

======================================================================
FAIL: test_invalid_inputs (test_factorial.TestLossModel.test_invalid_inputs)
Testing with invalid inputs (-ve numbers)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/mnt/Storage/Repositories/S208-DS-Python/labs/demo/test_factorial.py", line 25, in test_invalid_inputs
    self.assertEqual(None, fact(-10))
AssertionError: None != 1

----------------------------------------------------------------------
Ran 3 tests in 0.092s

FAILED (failures=1)
```