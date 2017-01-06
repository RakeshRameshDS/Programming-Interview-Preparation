"""

"""

arr = [5, -6, 7, 12, -3, 0, -11, 6]
arr = [-2, -3, 4, -1, -2, 1, 5, -3]

def max_sum_subsequence(arr):
    max_sum = 0
    curr_sum = 0
    for i in arr:
        curr_sum += i
        if curr_sum < 0:
            curr_sum = 0
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum

print(max_sum_subsequence(arr))