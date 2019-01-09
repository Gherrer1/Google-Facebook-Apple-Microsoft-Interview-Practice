def repeated_n_times(A):
    """
    :type A: List[int]
    :rtype: int
    """
    table = {}
    for num in A:
        table[num] = table.get(num, 0) + 1
        if table[num] > 1:
            return num
        
def repeated_n_times_constant_space(A):
    for i in range(len(A) - 2):
        if A[i] == A[i + 1] or A[i] == A[i + 2]:
            return A[i]
    return A[~0]