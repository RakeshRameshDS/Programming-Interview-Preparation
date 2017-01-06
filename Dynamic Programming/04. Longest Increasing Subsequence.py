"""
Find the longest increasing subsequence of a given array of numbers using dynamic programming.
"""

arr = [2, 7, 3, 4, 9, 8, 12]


def longest_increasing_subsequence(arr):
    dp = [1 for i in range(len(arr))]
    res_link = [-1 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j]:
                if dp[j]+1 > dp[i]:
                    res_link[i] = arr[j]
                dp[i] = max(dp[i], dp[j]+1)
    print(dp)
    print(res_link)
    return dp[-1]


print(longest_increasing_subsequence(arr))