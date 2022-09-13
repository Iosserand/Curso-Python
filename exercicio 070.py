#%%
continuar = ('')
material = ('')
soma = 0
cheap = 1000
cont = 0
while continuar != 'N':
    prod = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$'))
    soma += preco
    if preco > 1000:
        cont += 1 
    if preco < cheap:
        cheap = preco
        material = prod 
    continuar = str(input('Quer continuar? [S/N] ')).upper()
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {material} que custa R${cheap:.2f}')
# %%
