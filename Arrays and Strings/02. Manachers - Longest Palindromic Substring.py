"""
Manachers Algorithm - Longest Palindromic Substring
"""

S = "ABBAC"
def string_rep_change(S):
    sb = ''''''
    sb += "$"
    for i in S:
        sb += "#"+i
    sb += "#@"
    return sb

def manachers_algorithm(S):
    S = string_rep_change(S)
    dp = [0 for i in range(len(S))]
    center = 1; right = 1
    for i in range(len(S)-1):
        mirr = 2 * center - i # Very important formulae
        if i < right:
            dp[i] = min(right - i, dp[mirr])
        while S[i + (1 + dp[i])] == S[i - (1 + dp[i])]:
            dp[i] += 1
        if i + dp[i] > right:
            center = i
            right = i + dp[i]
    print(dp)
    return max(dp)

print(string_rep_change(S))
print(manachers_algorithm(S))