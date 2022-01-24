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
    n, s = abs(n), (n < 0)
    return uint2bytes((n - s) * 2 + s)

def bytes2int(bts):
    n, s = divmod(bytes2uint(bts), 2)
    return (n + s) * (-1) ** s

assert sum(int2bytes(36312488334073920)) == 1024
assert bytes2int([3]) == -2
