#%%
numeros_digitados = [[], []]
temporaria = []
for digito in range(1,8):
    num = int(input(f'Digite o {digito}º valor: '))
    if num % 2 == 0:
        numeros_digitados[0].append(num)
    else:
        numeros_digitados[1].append(num)


numeros_digitados[0].sort()
numeros_digitados[1].sort()
    
print('-='*30)
print(f'Os valores pares digitados foram {numeros_digitados[0]}')
print(f'Os valores ímpares digitados foram {numeros_digitados[1]}')
# %%
