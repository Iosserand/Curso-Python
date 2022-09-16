#%%
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end='')
    for vogais in palavra:
        if vogais == 'A':
            print(vogais.lower(), end=' ')
        elif vogais == 'E':
            print(vogais.lower(), end=' ')
        elif vogais == 'I':
            print(vogais.lower(), end=' ')
        elif vogais == 'O':
            print(vogais.lower(), end=' ')
        elif vogais == 'U':
            print(vogais.lower(), end=' ')
        
                
    
    




#%%
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS')
#letras_buscadas = ('a', 'e', 'i', 'o', 'u')
letras_buscadas = ('g')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end='')
    for letra in letras_buscadas:
        if letra in palavra.lower():
            print(letra, end=' ')
# %%
