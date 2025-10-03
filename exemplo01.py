valor_1 = 195 #11000011
valor_2 = 89  #01011001
              
              
'''

# Operações bit a bit (bitwise) com strings em Python
strTexto_1 = 'Programação'
strTexto_2 = 'desenvolver'

valor_1 & valor_2 = '01000001 - 65 and'
valor_1 | valor_2 = '11011011 - 219 ou'
valor_1 ^ valor_2 = '10011010 - 154 xor(ou exclusivo)'


texto_1 =  'P'
texto_2 =  'd'

op1=texto_1 and texto_2
#op2=texto_1 | texto_2
#op3=texto_1 ^ texto_2

print(ord(op1))


A ^ B = C ^ B = A
m     K   

'''
# Operações bit a bit (bitwise) com strings em Python
strTexto_1 = 'P'
strTexto_2 = 'd'


print(f'Texto 1................: {strTexto_1} -> ASCII = {ord(strTexto_1):>3}')
print(f'Texto 2................: {strTexto_2} -> ASCII = {ord(strTexto_2):>3}')

# Operação AND bit a bit (&)
andResultado = ord(strTexto_1) & ord(strTexto_2)
orResultado  = ord(strTexto_1) | ord(strTexto_2)
xorResultado = ord(strTexto_1) ^ ord(strTexto_2)
print(f'strTexto_1 & strTexto_2: ACSII = {andResultado:>3} -> {chr(andResultado)}')
print(f'strTexto_1 | strTexto_2: ACSII = {orResultado:>3} -> {chr(orResultado)}')
print(f'strTexto_1 ^ strTexto_2: ACSII = {xorResultado:>3} -> {chr(xorResultado)}')

#chr diz o caractere correspondente ao valor em ascii 
#ord diz o valor do da letra em ascii

