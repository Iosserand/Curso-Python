#%%

soma = 0
cont = 0
while True:
    n = int(input('Digite um número [999 para parar]')) 
    if n == 999:
        break
    soma = n + soma 

    cont += 1 
print('Você digitou {} números e a soma entre eles foi {}. '.format(cont, soma))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}. ')

    
# %%
