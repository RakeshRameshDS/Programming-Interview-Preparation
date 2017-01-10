arr1 = [i for i in range(1, 5)]
print(arr1)
arr2 = [i for i in range(2, 6)]
print(arr2)
def find_median(arr1, arr1_s, arr1_e, arr2, arr2_s, arr2_e):
    print(arr1_s, arr1_e, arr2_s, arr2_e)
    if arr1_s > arr1_e:
        return -1
    if arr1_s == arr1_e and arr2_s == arr2_e:
        return (arr1[arr1_s]+arr2[arr2_s])/2
    if arr1_e - arr1_s == 1 and arr2_e - arr2_s == 1:
        return (max(arr1[arr1_s], arr2[arr2_s]) + max(arr1[arr1_e], arr2[arr2_e]))/2
    m1 = int((arr1_s + arr1_e)/2)
    m2 = int((arr2_s + arr2_e)/2)
    print(m1, m2)
    if arr1[m1] == arr2[m2]:
        return arr1[m1]
    elif arr1[m1] > arr2[m2]:
        return find_median(arr1, arr1_s, m1-1, arr2, m2+1, arr2_e)
    else:
        return find_median(arr1, m1+1, arr1_e, arr2, arr2_s, m2-1)

print(find_median(arr1, 0, len(arr1)-1, arr2, 0, len(arr2)-1))