
#%%
continuar = ('')
maior = 0
man = 0
girl = 0
while continuar != 'N':
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    if idade > 18:
        maior += 1
    if sexo == 'M':
        man += 1
    if idade < 20 and sexo =='F':
        girl += 1
    continuar = str(input('Quer continuar? [S/N]')).upper()
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {man} homens cadastrados')
print(f'E temos {girl} mulheres com menos de 20 anos')
    

    

# %%
