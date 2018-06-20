## Merge Sort ##

def merge_sort(A):
    if len(A) <= 1: return A
    left_array,right_array = merge_sort(A[:int(len(A)/2)]),merge_sort(A[int(len(A)/2):])
    return merge(left_array, right_array)

def merge(A, B):
    c = []
    a_idx, b_idx =0, 0
    
    while a_idx < len(A) and b_idx < len(B):
        if A[a_idx] < B[b_idx]:
            c.append(A[a_idx])
            a_idx+= 1
        else:
            c.append(B[b_idx])
            b_idx+= 1

    if a_idx == len(A): c.extend(B[b_idx:])
    else: c.extend(A[a_idx:])
    return c

before_sort = [4,6,1,9,5,2,7,8]
print("before sort:", before_sort)
sorted_array = merge_sort(before_sort)
print("Merge Sorted array:", sorted_array)
            
        
