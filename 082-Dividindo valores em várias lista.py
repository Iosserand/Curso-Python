#%%
lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
for par in lista:
    if par % 2 == 0:
        pares.append(par)
    else:
        impares.append(par)
print('-='*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')

# %%
