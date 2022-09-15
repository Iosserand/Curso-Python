#%%
#import time
numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    digito = int(input('Digite um número entre 0 e 20: '))
    if digito > 20 or digito < 0:
        print('Tente novamente.')

    else: 
        print(f'Você digitou o número {numero[digito]}')
        #time.sleep(2)
        
        break
    
            
        

# %%
