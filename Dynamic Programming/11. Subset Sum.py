arr = [3, 2, 4, 19, 3, 7, 13, 10, 6, 11]

def subset_sum(arr, total):
    M = [[False for i in range(total+1)] for j in range(len(arr))]
    for i in range(len(arr)):
        for j in range(total+1):
            if j == 0 or j % arr[i] == 0:
                M[i][j] = True
            elif arr[i] > j:
                if i == 0:
                    M[i][j] = False
                else:
                    M[i][j] = M[i-1][j]
            else:
                M[i][j] = M[i-1][j] or M[i-1][j-arr[i]]
    for m in M:
        print(m)
    i = len(arr)-1; j = total
    selected = []
    while True:
        print(i, j, M[i][j], M[i-1][j], arr[i])
        if M[i][j] == M[i-1][j]:
            i -= 1
        else:
            selected.append(arr[i])
            j -= arr[i]
            i -= 1
        if i < 0 or j < 0:
            break
    print(selected)

    return M[-1][-1]

print(subset_sum(arr, 7))


