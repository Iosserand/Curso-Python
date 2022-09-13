#%%
cont = 0
media = 0
soma = 0
big = 10000
small = 0
while True:
    dig = str(input('Digite um número')).upper()
    if dig == 'N' or dig == 'S':
        break
    num = int(dig)
    cont += 1
    soma = num + soma
    media = soma/cont
    
    if num > small:
        big = num
    if num < big:
        small = num    
    
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {big} e o menor foi {2}')

# %%
