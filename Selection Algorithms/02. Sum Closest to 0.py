arr = [1, 60, -10, 70, -80, 85]

def closest_sum_2(arr):
    num1 = -9999; num2 = -9999
    pos_min = 9999; neg_min = -9999
    arr.sort()
    i = 0; j = len(arr)-1
    while i != j:
        temp = arr[i] + arr[j]
        if temp > 0:
            if abs(temp) < abs(pos_min):
                num1 = arr[i]; num2 = arr[j]
                pos_min = abs(temp)
            j -= 1
        else:
            if abs(temp) < abs(pos_min):
                num1 = arr[i]; num2 = arr[j]
                pos_min = abs(temp)
            i += 1
    return num1, num2, pos_min

print(closest_sum_2(arr))