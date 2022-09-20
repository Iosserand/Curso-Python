#%%
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar?'))
cont = 0
atual = 1
anterior = 0
proximo = 0
while cont < n:
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    print(anterior, end='')
    print(' -> ', end='')

    cont += 1
print('FIM')

# %%
