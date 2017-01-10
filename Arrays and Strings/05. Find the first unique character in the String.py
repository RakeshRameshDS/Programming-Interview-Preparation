S = "abcd abdf glmn"

def first_unique_character(S):
    dp = []
    pos = 0
    hm = {}
    for i in S:
        if not i.isalpha():
            continue
        if i in hm:
            dp[hm[i]] = False
        else:
            hm[i] = pos
            hm[pos] = i
            dp.append(True)
            pos += 1
    res = ''
    for i in range(len(dp)):
        if dp[i]:
            return hm[i]
            break
    return -1

print(first_unique_character(S))
