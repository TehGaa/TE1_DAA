# code is made by reference from conference paper
# https://epubs.siam.org/doi/epdf/10.1137/1.9781611975499.2

import numpy as np

def two_pivot_block_quicksort(A, low, high, B = 1024):
    if (high-low+1> 1 and low <= high):
        choose_pivot(A, low, high)
        i, j = block_lomuto(A, low,high, B)
        two_pivot_block_quicksort(A, low, i-1, B)
        two_pivot_block_quicksort(A,i+1, j-1, B)
        two_pivot_block_quicksort(A,j+1, high, B)


def block_lomuto(A, low, high,B):
    n = high - low + 1
    if (n > 1):
        p, q = A[low], A[high]
        block = [0] * B 
        i, j, k = low + 1, low + 1, 1
        
        num_less_than_p, num_less_equal_than_q = 0, 0

        while (k < n - 1):
            t = min(B, n - k - 1)

            for c in range(t):
                block[num_less_equal_than_q] = c
                num_less_equal_than_q += 1 if q >= A[k + c + low] else 0

            for c in range(num_less_equal_than_q):
                A[j + c], A[k + block[c] + low] = A[k + block[c] + low], A[j + c]

            k = k + t

            for c in range(num_less_equal_than_q):
                block[num_less_than_p] = c
                num_less_than_p += 1 if p > A[j + c] else 0

            for c in range(num_less_than_p):
                A[i], A[j + block[c]] = A[j + block[c]], A[i]
                i += 1

            j += num_less_equal_than_q
            num_less_equal_than_q, num_less_than_p = 0, 0 

        A[i - 1], A[low] = A[low], A[i - 1]
        A[j], A[high] = A[high], A[j]

        return i-1, j

# pivot by middle elements of array
def choose_pivot(A, low, high):
    left = (high + low)//2 
    right = left + 1

    if A[left] > A[right]:
        A[left], A[right] = A[right], A[left]

    A[low], A[left] = A[left], A[low]
    A[high], A[right] = A[right], A[high]

#testing
if __name__ == '__main__':
    arr = [1,0,1,2,1,3]
    two_pivot_block_quicksort(arr, 0, len(arr) -1)
    print(list(arr))

    arr = [1,9,2,8,3,7,4, 33, 6,5,888,777]
    two_pivot_block_quicksort(arr, 0, len(arr) -1)
    print(list(arr))

    arr = [9,8,7,6,5,4,3,2,1]
    two_pivot_block_quicksort(arr, 0, len(arr)-1)
    print(list(arr))

    arr = [1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1]
    two_pivot_block_quicksort(arr, 0, len(arr)-1)
    print(list(arr))