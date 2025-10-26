intA = 6
intB = 3

print(f'\n{intA} em binario é {bin(intA)}')
print(f'{intB} em binario é {bin(intB)}')

print(f'\nOperações bit a bit {intA} e {intB} :\n')
print(f'\t{intA} & {intB} = {intA & intB}')
print(f'\t{intA} | {intB} = {intA | intB}')
print(f'\t{intA} ^ {intB} = {intA ^ intB}')

print(f'\t~{intA} = {~intA}')
print(f'\t{intA} << 2 = {intA << 2}')
print(f'\t{intA} >> 1 = {intA >> 1}\n')