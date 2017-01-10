a = 5
b = 4

a += b
print(bin(a))
b = a - b
print(bin(b))
a = a - b
print(bin(a))
print(bin(-1))
print(a, b)


print("USING XOR")
a = 5
b = 4
print(bin(a), bin(b))
a ^= b
print(bin(a), bin(b))
b ^= a
print(bin(a), bin(b))
a ^= b
print(a, b)