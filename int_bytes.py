n = 1024
b = n.to_bytes(2, byteorder="big")
print(b)
print(int.from_bytes(b, "big"))

print(n.to_bytes(2, byteorder="little"))


b_big = b'\x04\x00'
b_little = b'\x00\x04'

print(int.from_bytes(b_big, "big"))
print(int.from_bytes(b_little, "little"))