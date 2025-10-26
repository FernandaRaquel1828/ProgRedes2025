bitMask =  0b0000100
bitValor = 0b00000001

bitValor |= bitMask
print(bin(bitValor))

if bitValor & bitMask:
    print('Bit 2 está ligado')

bitValor &= ~bitMask
print(bin(bitValor))

bitValor ^= bitMask
print(bin(bitValor))