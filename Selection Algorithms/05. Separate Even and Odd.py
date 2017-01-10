arr = [12, 34, 45, 9, 8, 90, 3]

# Even first, then odd
def sep_even_odd(arr):
    i = 0; j = len(arr)-1
    while i < j:
        while arr[i]%2 == 0:
            i += 1
        while arr[j]%2 == 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return arr

print(sep_even_odd(arr))