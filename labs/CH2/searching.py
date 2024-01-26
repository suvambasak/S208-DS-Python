

def linear_search(data_list: list[int], key: int) -> tuple[bool, int]:
    'Your code here'
    pass


def binary_search(
        data_list: list[int],
        key: int,
        left: int = None,
        right: int = None
) -> tuple[bool, int]:
    'Your code after if section'

    # Setting up left and right index
    if left == None and right == None:
        left = 0
        right = len(data_list)

    # Your code


def binary_recursive_search(
    data_list: list[int],
        key: int,
        left: int = None,
        right: int = None
) -> tuple[bool, int]:
    'Your code after if section'

    # Setting up left and right index
    if left == None and right == None:
        left = 0
        right = len(data_list)

    # Your code


if __name__ == '__main__':
    print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
    print(binary_recursive_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
