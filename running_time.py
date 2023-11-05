from two_pivot_block_quicksort import two_pivot_block_quicksort
from merge_sort import merge_sort
import sys
import time
sys.setrecursionlimit(1000000000)

def running_time_two_pivot_block_quicksort():
    print('-----TWO_PIVOT_BLOCK_QUICKSORT RUNNING TIME-----')
    ukuran  = ['kecil', 'sedang', 'besar']
    status = ['sorted', 'random', 'reversed']

    for i in ukuran:
        for j in status:
            file = open(f'dataset_{i}/{j}.txt', 'r')
            lst = []
            for line in file.readlines():
                lst.append(int(line))
            start_time = time.time()
            two_pivot_block_quicksort(lst, 0, len(lst)-1)
            end_time = time.time()
            print(f'Ukuran: {i}, Status: {j} = {(end_time - start_time) * 1000}')
            file.close()

def running_time_merge_sort():
    print('-----MERGE_SORT RUNNING TIME-----')
    ukuran  = ['kecil', 'sedang', 'besar']
    status = ['sorted', 'random', 'reversed']

    for i in ukuran:
        for j in status:
            file = open(f'dataset_{i}/{j}.txt', 'r')
            lst = []
            for line in file.readlines():
                lst.append(int(line))
            start_time = time.time()
            merge_sort(lst, 0, len(lst) - 1)
            end_time = time.time()
            print(f'Ukuran: {i}, Status: {j} = {(end_time - start_time) * 1000}')
            file.close()

def main():
    running_time_two_pivot_block_quicksort()
    print('\n\n')
    running_time_merge_sort()

if __name__ == '__main__':
    main()