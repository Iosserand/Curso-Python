#%%
def lin():
    print('-'*30)


#Programa principal
lin()
print('CURSO EM VIDEO')
lin()
print('APRENDA PYTHON')
lin()
print('LORD CENNABIS')
lin()


# %%
def titulo(msg):
    print('-'*30)
    print('{: ^25}'.format(msg))
    print('-'*30)

titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('LORD CENNABIS')
# %%
#PRÁTICA 
def soma(a, b):
    s = a + b 
    print(s)

#principal
soma(4, 8)
soma(9, 8)
soma(1, 2)

# %%
#PRÁTICA 
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b 
    print(f'A soma  A + B = {s}')

#principal
soma(4, 8)
soma(b=9, a=8)
soma(1, 2)
# %%
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
# %%
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos]*=2
        pos +=1

#principal
valores = [6, 3, 9, 1 , 0, 2]
dobra(valores)
print(valores)
# %%
#DESEMPACOTAMENTO
def soma(*valores):
    s = 0 
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
# %%
