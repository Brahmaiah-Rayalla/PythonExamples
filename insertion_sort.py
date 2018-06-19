## Insertion Sort ##

def insertion_sort(A):
    for i in range(1, len(A)):
        curr_num = A[i]
        for j in range(i-1, -1, -1):
            if A[j] > curr_num :
                A[j+1], A[j] = A[j], A[j+1]
            else:
                A[j+1] = curr_num
                break
    print(A)

insertion_sort([3, 2, 5, 1, 6, 4])
                
