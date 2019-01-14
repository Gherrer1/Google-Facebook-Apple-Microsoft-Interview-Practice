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
    