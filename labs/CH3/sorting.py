

def selection_sort(data_list: list[int]) -> None:
    '''
    data_list: unsorted list
    Return: None
    '''
    for start_index in range(len(data_list)):
        min_pos = start_index
        for min_index in range(start_index, len(data_list)):
            if data_list[min_index] < data_list[min_pos]:
                min_pos = min_index

        data_list[min_pos], data_list[start_index] = data_list[start_index], data_list[min_pos]


def insertion_sort(data_list: list[int]) -> None:
    '''
    data_list: unsorted list
    Return: None
    '''
    for start_index in range(len(data_list)):
        item = data_list[start_index]
        pos = start_index

        while pos > 0 and item < data_list[pos-1]:
            data_list[pos] = data_list[pos-1]
            pos -= 1
        data_list[pos] = item


def merge(list_1: list[int], list_2: list[int]) -> list[int]:
    '''
    list_1: sorted list
    list_2: sorted list
    Return: Merged sorted list
    '''
    merged_list = []
    index_1, index_2 = 0, 0

    while index_1 < len(list_1) and index_2 < len(list_2):

        if list_1[index_1] < list_2[index_2]:
            merged_list.append(list_1[index_1])
            index_1 += 1

        elif list_1[index_1] > list_2[index_2]:
            merged_list.append(list_2[index_2])
            index_2 += 1

        else:
            merged_list.append(list_1[index_1])
            merged_list.append(list_2[index_2])
            index_1 += 1
            index_2 += 1

    while index_1 < len(list_1):
        merged_list.append(list_1[index_1])
        index_1 += 1
    while index_2 < len(list_2):
        merged_list.append(list_2[index_2])
        index_2 += 1

    return merged_list


def merge_sort(data_list: list[int], lindex: int, rindex: int) -> list[int]:
    '''
    data_list: unsorted list
    lindex: left index i.e. starting index
    rindex: right index i.e. ending index

    Return: sorted list
    '''
    if rindex-lindex <= 1:
        return data_list[lindex: rindex]
    else:
        mid = (lindex+rindex)//2
        lhalf = merge_sort(data_list, lindex, mid)
        rhalf = merge_sort(data_list, mid, rindex)
        return merge(lhalf, rhalf)


def partition(data_list: list[int], lindex: int, rindex: int) -> int:
    '''
    data_list: unsorted list
    lindex: left index i.e. starting index
    rindex: right index i.e. ending index

    Return: pivot index
    '''
    big = lindex+1
    for small in range(lindex+1, rindex):
        if data_list[small] <= data_list[lindex]:
            data_list[big], data_list[small] = data_list[small], data_list[big]
            big += 1

    data_list[lindex], data_list[big-1] = data_list[big-1], data_list[lindex]
    return big-1


def quick_sort(data_list: list[int], lindex: int, rindex: int) -> None:
    '''
    data_list: unsorted list
    lindex: left index i.e. starting index
    rindex: right index i.e. ending index

    Return: Nothing
    '''

    if rindex-lindex <= 1:
        return
    else:
        pivot = partition(data_list, lindex, rindex)
        quick_sort(data_list, lindex, pivot)
        quick_sort(data_list, pivot+1, rindex)


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
