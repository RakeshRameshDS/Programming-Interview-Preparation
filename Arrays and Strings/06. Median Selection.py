import random
import numpy as np
rand_arr = []
for i in range(100):
    rand_arr.append(random.randint(0, 500))

print(rand_arr)
res = np.median(rand_arr)
print(res)


def median_find(arr):
    if len(arr) < 5:
        res = np.median(arr)
        return res
    else:
        li = []
        for i in range(int(len(arr)/5)):
            v1 = arr[5*i:5*i+5]
            v1.sort()
            pos = int(len(v1)/2)
            li.append(v1[pos])
        return median_find(li)
print(median_find(rand_arr))