#%%
matriz = []
valores = []
linha = 0 
coluna = 0 
while coluna < 3:
    while linha < 3:
        num = int(input(f'Digite um valor para [{coluna}, {linha}]: '))
        valores.append(num)
        matriz.append(valores[:])
        linha += 1
        valores.clear()
    coluna += 1
    linha = 0 
print('-='*30)
print(f'{matriz[0]}{matriz[1]}{matriz[2]}') 
print(f'{matriz[3]}{matriz[4]}{matriz[5]}')
print(f'{matriz[6]}{matriz[7]}{matriz[8]}')
# %%
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


# %%
