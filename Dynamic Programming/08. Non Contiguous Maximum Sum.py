arr = [3, 5, 8, 3, 9, 16, 32]

dp = {}
def sum_non_contiguous(arr, pos):
    global dp
    if pos == 0:
        dp[pos] = arr[pos]
        return arr[pos]
    elif pos in dp:
        return dp[pos]
    elif pos == 1:
        dp[pos] = max(arr[pos], arr[pos-1])
        return dp[pos]
    else:
        dp[pos] = max(arr[pos] + sum_non_contiguous(arr, pos-2), sum_non_contiguous(arr, pos-1))
        return dp[pos]

print(sum_non_contiguous(arr, len(arr)-1))
print(dp)