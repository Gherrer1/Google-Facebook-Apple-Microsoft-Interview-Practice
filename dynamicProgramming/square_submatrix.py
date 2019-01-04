def max_square_submatrix(M, r, c):
    if r < 0 or c < 0:
        return (0, 0, 0, 0)
    (_, upper_streak, _, global_n1) = max_square_submatrix(M, r - 1, c)
    (left_streak, _, _, global_n2) = max_square_submatrix(M, r, c - 1)
    global_n = max(global_n1, global_n2)

    if M[r][c] == False:
        return (0, 0, 0, global_n)
    
    (_, _, local_n, _) = max_square_submatrix(M, r - 1, c - 1)
    local_n = min(local_n + 1, left_streak + 1, upper_streak + 1)
    global_n = max(local_n, global_n)
    return (left_streak + 1, upper_streak + 1, local_n, global_n)

def max_square_submatrix_cache(M, r, c, cache):
    if r < 0 or c < 0:
        return (0, 0, 0, 0)
    if cache[r][c] != -1:
        return cache[r][c]
    (_, upper_streak, _, global_n1) = max_square_submatrix_cache(M, r - 1, c, cache)
    (left_streak, _, _, global_n2) = max_square_submatrix_cache(M, r, c - 1, cache)
    global_n = max(global_n1, global_n2)

    if M[r][c] == False:
        cache[r][c] = (0, 0, 0, global_n)
        return cache[r][c]

    (_, _, local_n, _) = max_square_submatrix_cache(M, r - 1, c - 1, cache)
    local_n = min(local_n + 1, left_streak + 1, upper_streak + 1)
    global_n = max(local_n, global_n)
    cache[r][c] = (left_streak + 1, upper_streak + 1, local_n, global_n)
    return cache[r][c]

def max_square_submatrix2(M, cache):
    global_n = 0

    for i in range(len(cache)):
        for j in range(len(cache[0])):
            if M[i][j] == True:
                left = 1
                upper = 1
                local_n = 1
                if i > 0:
                    upper = cache[i - 1][j][1] + 1
                if j > 0:
                    left = cache[i][j - 1][0] + 1
                if i > 0 and j > 0:
                    local_n = cache[i - 1][j - 1][2] + 1
                local_n = min(local_n, left, upper)
                global_n = max(local_n, global_n)
                cache[i][j] = (left, upper, local_n)
            else:
                cache[i][j] = (0, 0, 0)
    return global_n

matrix1 = [
    [True, True, True],
    [True, True, True],
    [True, False, True]
    ]
matrix2 = [
    [True,  False, False, False, False, False, False, False],
    [False, False, False, True,  True,  False, True,  True],
    [False, True,  True,  True,  True,  True,  True,  True],
    [False, True,  True,  True,  False, True,  True,  False],
    [False, True,  True,  True,  False, False, False, True]
]
matrix = matrix1
r = len(matrix) - 1
c = len(matrix[0]) - 1

cache = [[-1] * len(row) for row in matrix]
print max_square_submatrix_cache(matrix, r, c, cache)
# print max_square_submatrix2(matrix, cache)
