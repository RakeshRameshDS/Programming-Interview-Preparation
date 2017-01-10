arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]

def max_diff(arr):
    ld = [9999 for i in range(len(arr))]
    rd = [-9999 for i in range(len(arr))]
    for i in range(len(arr)):
        if arr[i] < ld[i]:
            ld[i] = arr[i]
        if i > 0 and ld[i] > ld[i-1]:
            ld[i] = ld[i-1]
    for i in reversed(range(len(arr))):
        if arr[i] > rd[i]:
            rd[i] = arr[i]
        if i < len(arr)-1 and rd[i] < rd[i+1]:
            rd[i] = rd[i+1]
    print(ld)
    print(rd)

max_diff(arr)