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

assert list(uint2bytes(624485)) == [0xE5, 0x8E, 0x26]
assert bytes2uint([205, 225, 178, 2]) == 5025997
