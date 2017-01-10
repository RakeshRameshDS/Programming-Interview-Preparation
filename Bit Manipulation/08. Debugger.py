num = 8

def debugger(num):
    val = num
    print(bin(val))
    val_prev = num - 1
    print(bin(val_prev))
    res = val & val_prev
    print(bin(res))

debugger(num)