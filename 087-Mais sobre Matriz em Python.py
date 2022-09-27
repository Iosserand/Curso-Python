#%%
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))


print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-='*30)


soma_pares = 0
soma_terceira_coluna = 0


for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            soma_pares += numero
        if numero == linha[2]:
            soma_terceira_coluna += numero
    if linha == matriz[1]:
        maior = max(linha)  


                
        
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior  dos valore da terceira coluna é {maior}')

# %%
