
#%%
import random
print('=-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-='*20)

resultado = ('').upper()
partida = ('').upper()
cont = 0
while partida != 'PERDEU':
    valor = int(input('Diga um valor: '))
    estado = str(input('Par ou Ímpar? [P/I]')).upper()
    pc = random.randint(0,10)   
    soma = valor + pc
    print('---'*20)
    if soma % 2 == 0:
        resultado = 'P'
        print(f'Você jogou {valor} e o computador {pc}. Total de {soma} DEU PAR ')
         
    else:
        resultado = 'I'
        print(f'Você jogou {valor} e o computador {pc}. Total de {soma} DEU ÍMPAR ')
        
    if estado == resultado:
        cont += 1
        partida = 'VENCEU'
        print(f'Você {partida}! ')
        print('Vamos jogar novamente...')

    else:
        partida = 'PERDEU'    
    print('---'*20)
        
print(f'Você {partida}! ')
print('=-='*20)
print(f'GAME OVER! Você venceu {cont} vezes')



# %%
