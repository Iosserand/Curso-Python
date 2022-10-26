#%%
from operator import itemgetter
from random import randint
from time import sleep

sorteio = {
'Jogador1':  randint(1,6),
'Jogador2':  randint(1,6),
'Jogador3':  randint(1,6),
'Jogador4':  randint(1,6),
}
print('Valores sorteados: ')
sleep(1)
for key, value in sorteio.items():
    print(f'{key} tirou {value} no dado. ')    
    sleep(1)
ranking = [] 
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)   
print('-='*30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)
# %%
    