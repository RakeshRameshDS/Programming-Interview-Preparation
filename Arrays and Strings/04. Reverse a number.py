a = 54321

def reverse_number(a):
    res = 0
    neg = False
    if a < 0:
        neg = True
        a *= -1
    temp_no = a
    while temp_no > 0:
        rem = temp_no % 10
        temp_no = int(temp_no / 10)
        res *= 10
        res += rem
    if neg:
        res *= -1
    return res

print(reverse_number(a))