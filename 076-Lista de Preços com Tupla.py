#%%
produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00)
print('-'*30)
print(f'Lista de compras')            
for pos , objt in enumerate(produtos): 
    if pos % 2 == 0:
        preco = produtos[pos+1]
        print(f'{objt:.<30}R${preco}')

# %%
