#%%
pessoas = {'nome': 'Iosserand', 'sexo': 'M', 'idade': 26}
print(pessoas)
print(pessoas['idade'])
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos. ')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in  pessoas.keys():
    print(k)

for k in  pessoas.values():
    print(k)

for k, v in  pessoas.items():
    print(f'{k} = {v}')

# %%
brasil = []
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'Bahia', 'sigla': 'BA'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
# %%
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
# %%
