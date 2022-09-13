#%%
print('Gerador de PA')
print('-=-'*10)
num1 = int(input('Primeiro termo: '))
num2= int(input('Razão da PA: '))
cont = 0
pa = num1
total = 0
seq = 10
while seq != 0:
    total = total + seq 
    while cont < total:
        print(pa, end='')
        pa = pa + num2
        print(' -> ', end='')
        cont += 1
    print('PAUSA') 
    seq = int(input('Quantos termos você quer mostrar a mais? '))   
print('Progressão finalizada com {} termos mostrados. '.format(cont))
# %%
