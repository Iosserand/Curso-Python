#%%
print('Gerador de PA')
print('-=-'*10)
num1 = int(input('Primeiro termo: '))
num2 = int(input('Razão da PA: '))
cont = 0
pa = num1
while cont < 10:
    print(pa, end='')
    pa = pa + num2
    print(' -> ', end='')
    cont += 1 
print('FIM')
# %%
