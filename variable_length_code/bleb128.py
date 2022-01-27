def uint2bytes(n):
    result = []
    while n > 127:
        result.append(n % 128 + 128)
        n = n // 128 - 1
    return bytearray(result + [n])

def bytes2uint(bts):
    num = -1
    for byte in reversed(bts):
        num = (num + 1) * 128 + (byte & 127)
    return num

assert list(uint2bytes(624485)) == [0xE5, 0x8D, 0x25]
assert bytes2uint([1, 2, 3]) == 65921

def int2bytes(n):
    result = []
    while abs(2*n + 1) > 128:
        n -= 64 * (-1) ** (n < 0)
        result.append(n % 128 + 128)
        n = n // 128
    return bytearray(result + [n % 128])

def bytes2int(bts):
    num = 0
    for byte in reversed(bts):
        num = num * 128 + (byte & 127)
    num -= 2**(7 * len(bts)) * (bts[-1] & 64 > 0)
    num += sum(64 * 128**p for p in range(len(bts) - 1)) * (-1) ** (num < 0)
    return num

assert sum(int2bytes(8256)) == 256
assert bytes2int([142, 42]) == 5454
