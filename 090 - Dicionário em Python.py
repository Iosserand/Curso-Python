#%%
boletim = {'nome': '', 'média': '', 'situação': '' }
nome = str(input('Nome: '))
media = int(input(f'Média de {nome}: '))
boletim['nome'] = nome
boletim['média'] = media
print('-='*30)
if media < 4:
    boletim['situação'] = 'Reprovado'
elif media <= 5:
    boletim['situação'] = 'Recuperação'
else:
    boletim['situação'] = 'Aprovado'
for key, value in boletim.items():
    print(f'- {key} é igual a {value}')


# %%
