texto1 =  "P"
texto2 = "f"

andResultado= ord(texto1) & ord(texto2)
orResultado= ord(texto1) | ord(texto2)
xorResultado= ord(texto1) ^ ord(texto2)
print(f"texto1 ............ {texto1} -> ASCII = {ord(texto1)} BIN = {ord(texto1):08b}")
print(f"texto2 ............ {texto2} -> ASCII = {ord(texto2)} BIN = {ord(texto2):08b}")
print(f"andResultado = {andResultado} caractere = {chr(andResultado)} BIN = {andResultado:08b}")
print(f"orResultado = {orResultado} caractere = {chr(orResultado)} BIN = {orResultado}")
print(f"xorResultado = {xorResultado} caractere = {chr(xorResultado)} BIN = {xorResultado}")
