#%%
num = [2, 5, 9, 1]
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 0)
print(num)
#num.pop(2)
#print(num)
num.insert(2, 2)
print(num)
num.remove(2)
print(num)
if 7 in num:
    num.remove(7)
else:
    print('Não achei o numero')



# %%
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...', end='\n')
print(f'Cheguei ao final da lista')
# %%
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
# %%
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista{a}')
print(f'Lista{b}')
# %%
