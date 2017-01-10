def get_pattern(pattern):
    res = [0 for i in range(len(pattern))]
    i = 1; j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            res[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = res[j-1]
        else:
            res[i] = 0
            i += 1
    return res


pattern = "ababaca"
res = get_pattern(pattern)
print(res)

string = "bacbabababacaca"

def check_str_pattern(string, pattern):
    P = get_pattern(pattern)
    i = 0; j = 0
    while i < len(string):
        if string[i] == pattern[j]:
            if j == len(pattern)-1:
                return i - j
            i += 1
            j += 1
        elif j > 0:
            j = P[j-1]
        else:
            i += 1
    return -1

print(check_str_pattern(string, pattern))