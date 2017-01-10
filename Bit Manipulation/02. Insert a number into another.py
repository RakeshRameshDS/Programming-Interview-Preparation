"""
You are given two numbers N and M and two bit positions i and j. Write a method to insert M into N such that M starts at bit j and ends at bit i
"""

def insert(N, M, i, j):
    mask1 = -1 << (j + 1)
    mask2 = (1 << i) - 1
    mask = mask1 | mask2
    N &= mask
    N |= (M << i)
    return N

N = 8
M = 3
i = 1; j = 2
print(insert(N,M,i,j))