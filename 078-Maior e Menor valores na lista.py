#%%
from multiprocessing.managers import ValueProxy


lista = list()
for numero in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {numero}: ')))
print('=-='*20)
print(f'Você digitou os valores {lista}') 
big = max(lista)
small = min(lista)   
print(f'O maior valor digitado foi {big} na posição ', end=' ')
for posicao, valor in enumerate(lista):
    if valor == big:
        print(f'{posicao}...', end=' ')
print(f'\nO menor posicao digitado foi {small} na posição ', end=' ')
for posicao, valor in enumerate(lista):
    if valor == small:
        print(f'{posicao}...', end=' ')

# %%
