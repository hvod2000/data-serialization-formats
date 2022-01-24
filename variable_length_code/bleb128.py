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
