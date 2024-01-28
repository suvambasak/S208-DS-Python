import sys
from ignore_sorting import insertion_sort, selection_sort, merge_sort, quick_sort
sys.setrecursionlimit(1000000)

# num_list = [i for i in range(30000)]
num_list = [i for i in range(30000, 0, -1)]

selection_sort(num_list)
insertion_sort(num_list)
merge_sort(num_list, 0, len(num_list))
quick_sort(num_list, 0, len(num_list))
