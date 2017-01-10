"""
GetBit
"""

def get_bit(num, bit):
    return (num & (1 << bit)) != 0

def set_bit(num, bit):
    return (num | (1 << bit))

def clear_bit(num, bit):
    return num & ~(1 << bit)

def clear_all_bits_msb(num, bit):
    mask = (1 << bit) - 1
    return num & mask

def clear_all_bits_lsb(num, bit):
    mask = -1 << (bit + 1)
    return num & mask

print(get_bit(8, 3))