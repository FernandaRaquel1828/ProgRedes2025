intValor = 1024

print(intValor.to_bytes(2, byteorder="big"))
print(intValor.to_bytes(2, byteorder="little"))

import sys

print(sys.byteorder)