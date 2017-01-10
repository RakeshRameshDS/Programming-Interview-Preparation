"""
Problem:
Given an array of size n, find a peak element in the array.
For example:
In Array [1,4,3,6,7,5] 4 and 7 are Peak Elements. Return any one Peak Element.
"""

arr = [3, 4, 5, 4, 7, 1]

def find_peak(arr, start, end):
    if start > end:
        return -9999
    else:
        mid = int((start + end)/2)
        if mid - 1 < 0 and arr[mid] >= arr[mid + 1]:
            return arr[mid]
        elif mid + 1 >= len(arr) and arr[mid] >= arr[mid-1]:
            return arr[mid]
        elif arr[mid] >= arr[mid-1] and arr[mid] >= arr[mid+1]:
            return arr[mid]
        else:
            if arr[mid-1] > arr[mid]:
                return find_peak(arr, start, mid-1)
            else:
                return find_peak(arr, mid+1, end)

print(find_peak(arr, 0, len(arr)))