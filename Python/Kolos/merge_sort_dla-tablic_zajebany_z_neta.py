def merge_sort(A):
    if len(A)>1:
        dziel=len(A)//2
        left=A[:dziel]
        right=A[dziel:]
        merge_sort(left)
        merge_sort(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
