num = 80
arr = [23, 15, 77, 80, 80, 80, 90]

def bin_search(arr, start, end, num):
    if start > end:
        return -1
    else:
        mid = int((start + end)/2)
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            return bin_search(arr, start, mid-1, num)
        else:
            return bin_search(arr, mid + 1, end, num)

def find_num_count(arr, num):
    pos = bin_search(arr, 0, len(arr)-1, num)
    i = pos-1; j = pos+1
    counter = 1
    while i >= 0 and arr[i] == num:
        i -= 1
        counter += 1
    while j < len(arr) and arr[j] == num:
        j += 1
        counter += 1
    return counter


print(find_num_count(arr, num))
