# 944 on Leetcode
def min_deletion_size(self, A):
    """
    :type A: List[str]
    :rtype: int
    """
    if len(A) == 0 or len(A[0]) == 0:
        return 0

    num_unsorted_cols = 0
    common_str_len = len(A[0])
    for i in range(common_str_len):
        for j in range(len(A) - 1):
            if A[j][i] > A[j + 1][i]:
                num_unsorted_cols += 1
                break
    return num_unsorted_cols