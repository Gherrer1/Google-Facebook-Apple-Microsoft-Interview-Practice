def merge(arr, start, middle, end):
    sorted_arr = []

    i = start
    j = middle + 1
    while i <= middle and j <= end:
        if arr[i] < arr[j]:
            sorted_arr.append(arr[i])
            i += 1
        else:
            sorted_arr.append(arr[j])
            j += 1
    while i <= middle:
        sorted_arr.append(arr[i])
        i += 1
    while j <= end:
        sorted_arr.append(arr[j])
        j += 1
    i = start
    for num in sorted_arr:
        arr[i] = num
        i += 1

def merge_sort(arr, start, end):
    if len(arr) == 0 or start >= end: return
    middle = (start + end) / 2
    merge_sort(arr, start, middle)
    merge_sort(arr, middle + 1, end)
    merge(arr, start, middle, end)
    
testArr1 = []
testArr2 = [4]
testArr3 = [9, 5]
testArr4 = [100, 7, 3, 25, 60, 355, 24, 1, 56, 12, 3, 500, 9134, 91, 211]
testArr5 = [100, 7, 3, 25, 60, 45, 355, 24, 1, 56, 12, 3, 500, 9134, 91, 211]

print merge_sort(testArr1, 0, len(testArr1) - 1) or testArr1 # expect []
print merge_sort(testArr2, 0, len(testArr2) - 1) or testArr2 # expect [4]
print merge_sort(testArr3, 0, len(testArr3) - 1) or testArr3 # expect [5, 9]
print merge_sort(testArr4, 0, len(testArr4) - 1) or testArr4 # expect [3, 7, 25, 60, 100]
print merge_sort(testArr5, 0, len(testArr5) - 1) or testArr5 # expect [3, 7, 25, 45, 60, 100]