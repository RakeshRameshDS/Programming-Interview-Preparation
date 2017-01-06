"""
Given two strings X[m] and Y[n], find the longest common subsequence of the two given strings.
A sub sequence is a sequence that appears in the same relative order, but not necessarily contiguous.
example
X= T A B A E D A     Y= C A N B H A E U Y A
LCS = { ABAEA }
"""

X = "TABAEDA"
Y = "CANBHAEUYA"


def longest_common_subsequence(X, Y):
    res = ''''''
    dp = [[0 for i in range(len(Y))] for j in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y)):
            if i == 0 and j == 0:
                pass
            elif i == 0:
                if X[i] == Y[j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1]
            elif j == 0:
                if X[i] == Y[j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                if X[i] == Y[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    for k in dp:
        print(k)
    return res

longest_common_subsequence(X, Y)