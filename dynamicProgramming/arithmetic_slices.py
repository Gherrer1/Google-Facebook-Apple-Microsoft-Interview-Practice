# 413 on Leetcode
def num_arithmetic_slices(arr):
    if len(arr) < 3:
        return 0

    num_slices = 0
    length = 2
    diff = arr[1] - arr[0]

    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] == diff:
            length += 1
            num_slices += (length - 2)
        else:
            length = 2
            diff = arr[i] - arr[i - 1]
    return num_slices

test1 = [0, 0, 0, 1, 2, 3, 4, 5, 5, 5, 6, 7]
test2 = [0, 0, 0]
test3 = [0, 0, 1]
test4 = [0, 0]

print num_arithmetic_slices(test1) # expect 13
print num_arithmetic_slices(test2) # expect 1
print num_arithmetic_slices(test3) # expect 0 
print num_arithmetic_slices(test4) # expect 0