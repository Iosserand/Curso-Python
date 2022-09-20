#%%
numeros = list()

while True:
    entrada = int(input('Digite um valor: '))
    if entrada not in numeros:
        numeros.append(entrada)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    checkpoint = str(input('Quer continuar? [S/N] ')).upper()

    if checkpoint == "N":
        break
        
print('-=-'*20)
print(f"Você digitou os valores {sorted(numeros)}")
# %%
