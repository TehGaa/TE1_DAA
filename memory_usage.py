from two_pivot_block_quicksort import two_pivot_block_quicksort
from merge_sort import merge_sort
import numpy as np
import sys
import tracemalloc
from memory_profiler import memory_usage

sys.setrecursionlimit(1000000000)

def memory_usage_two_pivot_block_quicksort():
    print('-----TWO_PIVOT_BLOCK_QUICKSORT MEMORY USAGE-----')
    ukuran  = ['kecil', 'sedang', 'besar']
    status = ['sorted', 'random', 'reversed']

    for i in ukuran:
        for j in status:
            file = open(f'dataset_{i}/{j}.txt', 'r')
            lst = []
            for line in file.readlines():
                lst.append(int(line))
            tracemalloc.start()
            two_pivot_block_quicksort(lst, 0, len(lst) - 1)
            print(f'Ukuran: {i}, Status: {j} = {tracemalloc.get_traced_memory()}')
            tracemalloc.stop()
            file.close()

def memory_usage_merge_sort():
    print('-----MERGE_SORT MEMORY USAGE-----')
    ukuran  = ['kecil', 'sedang', 'besar']
    status = ['sorted', 'random', 'reversed']

    for i in ukuran:
        for j in status:
            file = open(f'dataset_{i}/{j}.txt', 'r')
            lst = []
            for line in file.readlines():
                lst.append(int(line))
            tracemalloc.start()
            merge_sort(lst, 0, len(lst) - 1)
            print(f'Ukuran: {i}, Status: {j} = {tracemalloc.get_traced_memory()}')
            tracemalloc.stop()
            file.close()

def main():
    memory_usage_two_pivot_block_quicksort()
    print('\n\n')
    memory_usage_merge_sort()

if __name__ == '__main__':
    main()