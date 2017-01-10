arr = [1, 5, 3, 7, 19, 4]

def three_sum(arr, val):
    arr.sort()
    num1 = 99999; num2 = 999999; num3 = 999999
    for k in range(len(arr)):
        i = k+1; j = len(arr)-1
        while i < j:
            if arr[k] + arr[i] + arr[j] == val:
                num1 = arr[k]; num2 = arr[i]; num3 = arr[j]
                break
            elif arr[k] + arr[i] + arr[j] < val:
                i += 1
            else:
                j -= 1
        if num1 != 99999:
            break
    return num1, num2, num3

print(three_sum(arr, 12))