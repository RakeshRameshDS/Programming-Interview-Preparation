nums = [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 6, 7]
XOR = 0
for i in range(-7, 8):
    XOR ^= i
print(XOR)
print(bin(XOR))

XOR1 = 0
for i in nums:
    XOR ^= i
print(XOR)
print(bin(XOR))

right_most_bit = XOR & ~(XOR-1)
print(right_most_bit)
X = 0; Y = 0
for i in nums:
    if i & right_most_bit:
        X = X^i
    else:
        Y = Y^i

for j in range(-7, 8):
    if j & right_most_bit:
        X ^= j
    else:
        Y ^= j

print(X, bin(X))
print(Y, bin(Y))
