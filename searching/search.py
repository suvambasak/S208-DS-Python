
from ignore_searching import linear_search, binary_search

sorted_list = [i for i in range(90000000)]


print(linear_search(sorted_list, sorted_list[-1]))
print(binary_search(sorted_list, sorted_list[-1]))
