def bytes2bits(bytes: int) -> int:
    return bytes * 8
def bits2bytes(bits: int) -> int:
    return bits // 8
intBytes = 4
intBits = 64
print(f'{intBytes} bytes = {bytes2bits(intBytes)} bits')
print(f'{intBits} bits = {bits2bytes(intBits)} bytes')