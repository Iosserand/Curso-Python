#%%
lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = str(input(f'Quer continuar?'))
    if continuar in 'Nn':
        break
lista.sort(reverse=True)   
print(f'Você digitou {len(lista)} elementos.')
print(f'O valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')


# %%
