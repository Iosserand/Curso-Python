#%%
cadastros = list()
pessoas = list()
pesos = list()
nomes = list()
# input_de_pessoas = [['ze', 21], ['ana', 89], ['eli', 89]]

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dado_pessoa = [nome, peso][:]
    pessoas.append(dado_pessoa)
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break


for pessoa in pessoas:
    nomes.append(pessoa[0])
    pesos.append(pessoa[1])

max_peso = max(pesos)
min_peso = min(pesos)
# indice_do_maior_peso = pesos.index(max_peso)     
# indice_do_menor_peso = pesos.index(min_peso)
# nome_maior_peso = nomes[indice_do_maior_peso]  
# nome_menor_peso = nomes[indice_do_menor_peso]   


print('-='*30)
# print(pessoas)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas. ')
print(f'O maior peso foi de {max_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == max_peso:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {min_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == min_peso:
        print(f'{p[0]} ', end='')


# %%
