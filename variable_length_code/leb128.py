def uint2bytes(n):
    result = []
    while n > 127:
        n, r = divmod(n, 128)
        result.append(r + 128)
    return bytearray(result + [n])

def bytes2uint(bts):
    num = 0
    for byte in reversed(bts):
        num = num * 128 + (byte & 127)
    return num

def int2bytes(n):
    result = []
    while abs(2*n + 1) > 128:
        n, r = divmod(n, 128)
        result.append(r + 128)
    return bytearray(result + [n % 128])

def bytes2int(bts):
    num = 0
    for byte in reversed(bts):
        num = num * 128 + (byte & 127)
    M = 2**(7 * len(bts) - 1)
    return (M + num) % (2*M) - M

assert list(uint2bytes(624485)) == [0xE5, 0x8E, 0x26]
assert bytes2uint([0xCD, 0xE1, 0xB2, 0x02]) == 5025997
assert list(int2bytes(-123456)) == [0xC0, 0xBB, 0x78]
assert bytes2int([0x9B, 0xF1, 0x59]) == -624485
