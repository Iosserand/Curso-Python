#%%
import time
cont = 0
while True:
    #print('-'*20)     
    num = int(input('Quer ver a tabuada de Qual Valor ? '))
    print(f'Quer ver a tabuada de Qual Valor ? {num}')
    print('-'*20)
    if  num < 0:
        break
    while cont < 10:
        cont += 1
        print(f'{num} x {cont} = {num*cont}')
        #time.sleep(1)
    print('-'*20)
    cont = 0    
   
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
# %%
