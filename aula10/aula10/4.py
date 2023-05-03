num = input('Digite um num binario: ')
base = int(input('Qual a base? [2] [8] [16] '))
n = len(num) - 1
decimal = 0

digitos = '0123456789ABCDEF'

for b in num:
    decimal = decimal + digitos.find(b)*base**n
    n = n - 1

print(decimal)    