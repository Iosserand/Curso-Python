num = int(input('Digite em um número para calcular seu Fatorial: '))
cont = num
fat = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat = cont * fat
    cont -= 1
print('{}'.format(fat))
