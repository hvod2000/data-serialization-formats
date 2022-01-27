def gen_bleb(base):
    def uint2bytes(n):
        result = []
        while n + base > 255:
            n -= 256 - base
            n, r = divmod(n, base)
            result.append(r + 256 - base)
        return bytearray(result + [n])

    def bytes2uint(bts):
        num = bts[-1]
        for byte in reversed(bts[:-1]):
            num = num * base + byte
        return num
    return uint2bytes, bytes2uint

uint2bytes, bytes2uint = gen_bleb(246)
assert list(uint2bytes(1234)) == [250, 4]
assert bytes2uint(uint2bytes(1234567)) == 1234567
