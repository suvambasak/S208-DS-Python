

def selection_sort(data_list: list[int]) -> None:
    '''
    data_list: unsorted list
    Return: None
    '''
    pass  # Your code here


def insertion_sort(data_list: list[int]) -> None:
    '''
    data_list: unsorted list
    Return: None
    '''
    pass  # Your code here


def merge(list_1: list[int], list_2: list[int]) -> list[int]:
    '''
    list_1: sorted list
    list_2: sorted list
    Return: Merged sorted list
    '''
    pass  # Your code here


def merge_sort(data_list: list[int], lindex: int, rindex: int) -> list[int]:
    '''
    data_list: unsorted list
    lindex: left index i.e. starting index
    rindex: right index i.e. ending index

    Return: sorted list
    '''
    pass  # Your code here


def partition(data_list: list[int], lindex: int, rindex: int) -> int:
    '''
    data_list: unsorted list
    lindex: left index i.e. starting index
    rindex: right index i.e. ending index

    Return: pivot index
    '''
    pass  # Your code here


def quick_sort(data_list: list[int], lindex: int, rindex: int) -> None:
    '''
    data_list: unsorted list
    lindex: left index i.e. starting index
    rindex: right index i.e. ending index

    Return: Nothing
    '''

    pass  # Your code here


if __name__ == '__main__':
    data_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 5]

    selection_sort(data_list)
    insertion_sort(data_list)
    data_list = merge_sort(data_list, 0, len(data_list))
    quick_sort(data_list, 0, len(data_list))

    print(data_list)

    print(
        merge(
            [1, 3, 5, 7, 9],
            [0, 2, 4, 6, 8, 10]
        )
    )

    print(partition(data_list, 0, len(data_list)))
    print(data_list)
