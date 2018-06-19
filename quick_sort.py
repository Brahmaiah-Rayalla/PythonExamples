## Quick Sort ##
from random import randint
def quick_sort(A):
    print ("unsorted array: ", A)
    if len(A) <= 1 : return A
    smaller, equal, larger = [], [], []
    pivot = A[randint(0, len(A)-1)]
    for i in A:
        if i < pivot: smaller.append(i)
        elif i == pivot: equal.append(i)
        else:
            larger.append(i)
    return quick_sort(smaller) + equal + quick_sort(larger)

## create randomized , unsorted array for testing
#def create_array(size=10, max = 50):
    #return [randint(0, max) for _ in range(size)]

sorted_array = quick_sort([3,1,6,5,4,2,9])

print ("sorted array: ", sorted_array)
