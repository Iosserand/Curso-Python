#%%
from time import sleep

pessoas = []
nomes = []
notas = []

while True:
    nome = str(input(f'Nome: '))
    nomes.append(nome[:])
    for n in range(1,3):
        notas.append(int(input(f'Nota{n}: ')))
    
    nomes.append(notas[:])
    pessoas.append(nomes[:])
    notas.clear()
    nomes.clear()
     
    continuar = str(input(f'Quer continuar ? '))
    # print(pessoas)
    if continuar in 'Nn':
        break
print('-='*30)
print(f'No.     NOME    MÉDIA')
print('--'*15)
for numero, registro in enumerate(pessoas):
    print(f'{numero}        {registro[0]}     {sum(registro[1])/len(registro[1]):>4}')
print('--'*15)
while True:
    escolha = int(input(f'Mostrar notas de qual aluno? (999 interrompe) '))
    for numero, registro in enumerate(pessoas):
        if numero == escolha:
            print(f'Notas de {registro[0]} são {registro[1]} ')
        
    if escolha == 999:
        break
print(f'FINALIZANDO...')
sleep(1)
print(f'<<< VOLTE SEMPRE >>>')
# %%