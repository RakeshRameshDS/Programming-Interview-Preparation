num = 0.101

def binary_rep(num):
    binary = ''''''
    binary += '.'
    while (num > 0 and num > 1e-6):
        if len(binary) > 32:
            print("ERROR")
            break
        r = num * 10
        if r >= 1:
            binary += str(1)
            num = r - 1
        else:
            binary += str(0)
            num = r
    return binary

print(binary_rep(num))