def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):                  # from 1 to n-1
        cur = A[k]                              # current element to be inserted
        j = k                                   # find current index j for current
        while j > 0 and A[j-1] > cur:         # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
            A[j] = cur                              # cur is now in the right place
        return None
    return A

print(insertion_sort([6, 7, 2, 9, 1, 0]))