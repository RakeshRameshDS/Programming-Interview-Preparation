
dp = {}
def catalan(num):
    dp = {}
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, num+1):
        dp[i] = 0
        for j in range(0, i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[num]

print(catalan(4))