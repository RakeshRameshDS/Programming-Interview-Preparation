arr = [-17, 3, 8, 12, 4, 10, 5]

def zero_sum(arr):
    min_val = 9999
    num1 = 9999; num2 = 9999; num3 = 9999
    for k in range(len(arr)):
        i = k + 1; j = len(arr)-1
        while i < j:
            S = arr[k] + arr[i] + arr[j]
            if S == 0:
                num1 = arr[k]; num2 = arr[i]; num3 = arr[j]
                return num1, num2, num3, 0
            elif S < 0:
                if abs(S) < abs(min_val):
                    num1 = arr[k]
                    num2 = arr[i]
                    num3 = arr[j]
                    min_val = S
                i += 1
            else:
                if abs(S) < abs(min_val):
                    num1 = arr[k]
                    num2 = arr[i]
                    num3 = arr[j]
                    min_val = S
                j -= 1
    return num1, num2, num3, min_val

print(zero_sum(arr))