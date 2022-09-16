#%%
primeiro = int(input('Digite um número: '))
segundo = int(input('Digite outro número: '))
terceiro = int(input('Digite mais um número: '))
ultimo = int(input('Digite o último número: '))
tupla = (primeiro, segundo, terceiro, ultimo)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes ')
existe_numero_tres = False
for numero in tupla:
    if numero == 3:        
        existe_numero_tres = True   
        
if existe_numero_tres is True:
    print(f'O valor 3 apareceu na {(tupla.index(3))+1}ª posição ')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição ')
print(f'Os valores pares digitados foram ', end='') 
for numero in tupla:
    if numero % 2 == 0:
        print(f'{numero} ', end='')

        

    

# %%
