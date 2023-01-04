#%%
#numeros = [1, 9, 7, 4, 5, 8, 6, 2, 3]
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#numeros = [9, 8, 7, 6, 5, 4, 3, 2, 1]
numeros = [1, 2, 3, 4, 5, 6, 7, 9, 8]
cont = 0
cont2 = 0

for i in range(len(numeros)):
    sair = True
    #print(i, end=' ')
    j = ((len(numeros)- i)-1)
    #print(f'i = {i} e j = {j}')
    for k in range(j):
        atual = numeros[k]
        proximo = numeros[k+1]
        cont += 1
        if atual > proximo:
            numeros[k] = proximo
            numeros[k+1] = atual
            cont2 += 1
            sair = False
    if sair == True:
        break
print(numeros, end= ' ')
print(cont)
print(cont2)

# %%
