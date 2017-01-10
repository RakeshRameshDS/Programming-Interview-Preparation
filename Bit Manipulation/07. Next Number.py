num = 1775
print(bin(num))


def getNext(num):
    temp = num
    prev = 0
    counter = 0
    while temp != 0:
        temp >>= 1
        res = (temp & 1)
        counter += 1
        if res == 0 and prev == 1:
            break
        elif res == 1:
            prev = 1
    mask = 1 << counter
    num |= mask
    mask = 1 << (counter-1)
    num &= ~mask
    return num


def getPrev(num):
    temp = num
    prev = 0
    counter = 0
    while temp != 0:
        temp >>= 1
        res = (temp & 1)
        counter += 1
        if res == 0 and prev == 1:
            break
        elif res == 1:
            prev = 1
    mask = 1 << (counter+1)
    num &= ~mask
    mask = 1 << counter
    num |= mask
    return num

res = getNext(num)
print(bin(res))

print()
print(bin(num))
res = getPrev(num)
print(bin(res))