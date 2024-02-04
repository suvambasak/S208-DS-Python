

def linear_search(data_list: list[int], key: int) -> tuple[bool, int]:
    '''Linear search in a list

    Parameters
    ----------
    data_list: list[int]
        input list
    key: int
        element to search for

    Returns
    ---------
    tuple(True/False, int)
        Status and index
    '''
    pass  # Your code here


def binary_search(
        data_list: list[int],
        key: int,
        left: int = None,
        right: int = None
) -> tuple[bool, int]:
    '''Binary search (iterative) in a list

    Parameters
    ----------
    data_list: list[int]
        input list
    key: int
        element to search for
    left: int, optional
        left index of the list
    right: int, optional
        right index of the list


    Returns
    ---------
    tuple(True/False, int)
        Status and index
    '''

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
    '''Binary search (recursive) in a list

    Parameters
    ----------
    data_list: list[int]
        input list
    key: int
        element to search for
    left: int, optional
        left index of the list
    right: int, optional
        right index of the list


    Returns
    ---------
    tuple(True/False, int)
        Status and index
    '''

    # Setting up left and right index
    if left == None and right == None:
        left = 0
        right = len(data_list)

    # Your code


if __name__ == '__main__':
    print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
    print(binary_recursive_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
