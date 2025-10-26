print((0).bit_length())
print((5).bit_length())
print((255).bit_length())

intValor = 1023
print(intValor.bit_length())

bits = intValor.bit_length()
intBytesNeed =(bits + 7) // 8
print(intBytesNeed)