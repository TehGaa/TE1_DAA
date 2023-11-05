# code is made by reference from geeks for geeks
# https://www.geeksforgeeks.org/python-program-for-merge-sort/
# author didn't reference from slide for the sake of simplicity
# (slide merge sort pseudocode needs a very large number for the 
# last element of list L and R)
import numpy as np

def merge_sort(A,p,r):
    if (p < r):
        q = (p + r)//2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + j + 1]
    
    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

#testing
if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1]
    merge_sort(arr, 0, len(arr)-1)
    print(list(arr))