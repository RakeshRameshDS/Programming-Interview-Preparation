arr = [7, 10, 14, 15, 16, 19, 20, 25, 1, 3, 4, 5]

def find_pivot(arr, start, end):
    print(start, end)
    if start > end:
        return -1, -1
    elif start == end:
        return arr[start], start
    else:
        mid = int((start + end)/2)
        if arr[mid] < arr[start]:
            return find_pivot(arr, start, mid)
        else:
            return find_pivot(arr, mid + 1, end)

print(find_pivot(arr, 0, len(arr)-1))