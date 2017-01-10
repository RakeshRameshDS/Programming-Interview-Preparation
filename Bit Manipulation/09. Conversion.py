num1 = 29
num2 = 15

print(bin(num1))
print(bin(num2))

def convert(num1, num2):
    counter = 0
    while num1 != 0 and num2 != 0:
        if (num1 & 1) != (num2 & 1):
            counter += 1
        num1 >>= 1
        num2 >>= 1
    val = num1 if num1 != 0 else num2
    while val != 0:
        if val & 1 == 1:
            counter += 1
        val >>= 1
    return counter

def convert_efficient(num1, num2):
    res = num1 ^ num2
    counter = 0
    while res != 0:
        if res & 1 == 1:
            counter += 1
        res >>= 1
    return counter



print(convert(num1, num2))
print(convert_efficient(num1, num2))

num = 0xaaaa
print(bin(num))
num = 0x5555
print(bin(num))