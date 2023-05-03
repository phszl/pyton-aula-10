decimal = int(input('Digite um numero decimal: '))
print('[2] Binário/n [8] Octal/n [16] Hexadecimal')
base = int(input('Qual a base? [2] [8] [16]: '))

digitos = '0123456789ABCDEF'

convertido = ''
while decimal > 0:
    convertido = str(digitos[decimal%base]) + convertido
    decimal = decimal//base

print(convertido)
