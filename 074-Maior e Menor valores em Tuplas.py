#%%
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
                randint(1, 10),randint(1, 10))
print(f'Os valores sorteados foram: {numeros}') 
big = 1
small = 1000 
for size in numeros:
    if big < size:
        big = size
    elif small > size:
        small = size
print(f'O maior valor sorteado foi {big}')
print(f'O menor valor sorteado foi {small}')
# %%







#%%
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
                randint(1, 10),randint(1, 10))
print(f'Os valores sorteados foram: ', end='') 
for size in numeros:
    print(f'{size} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
# %%
