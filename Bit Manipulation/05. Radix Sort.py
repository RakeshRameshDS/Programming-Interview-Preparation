"""
Radix Sort
"""
import random

limit = 600
num_digits = 3
nums = [i for i in range(-limit + 1,limit)]
for _ in range(4):
    rand = random.randint(-500,500)
    print(rand)
    nums.remove(rand)
print()
print()

def radix_sort(nums, radix):
    ex_10 = 10
    for j in range(radix):
        hm = [[] for i in range(10)]
        for num in nums:
            mask = pow(ex_10, j)
            nm = abs(int(num / mask))
            val = nm % 10
            hm[val].append(num)
        sign = [[] for i in range(2)]
        nums.clear()
        for k in range(len(hm)):
            for ele in hm[k]:
                if ele >= 0:
                    sign[1].append(ele)
                else:
                    sign[0].append(ele)
        sign[0].reverse()
        for k in range(2):
            nums.extend(sign[k])
    for k in range(len(nums)):
        if nums[k] - nums[k-1] > 1:
            print(nums[k-1]+1)
    return nums

#radix_sort(nums, radix=3)
nums = [-3, -2, -1, 0, 1, 2, 3, 4, 70, -659, -33, 840]

def radix_sort_bin(nums):
    mx = max(nums)
    radix = len(bin(mx))
    for i in range(radix):
        zeroes = []
        ones = []
        for pos in range(len(nums)):
            val = nums[pos]
            bit = (val >> i) & 1
            if bit == 0:
                zeroes.append(val)
            else:
                ones.append(val)
        zeroes.extend(ones)
        nums = zeroes
    return nums

print(radix_sort_bin(nums))

