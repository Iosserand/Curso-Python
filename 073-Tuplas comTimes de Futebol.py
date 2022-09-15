#%%
brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print('-=-'*25)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-=-'*25)
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print('-=-'*30)
print(f'Os 4 últimos são {brasileirao[-1:-5:-1]}')
print('-=-'*30)
print('Times em ordem alfabética: {}'.format(sorted(brasileirao)))
print('-=-'*30)
print('O Cruzeiro está na {}º posição'.format(brasileirao.index('Cruzeiro')))

# %%
