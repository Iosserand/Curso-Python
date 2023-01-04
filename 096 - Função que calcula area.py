#%%
def titulo(msg):
    print('{:^5}'.format(msg))


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a} m².')    


#PROGRAMA
titulo('Controle de Terrenos')
titulo('-'*30)
largura = float(input(f'LARGURA (m): '))
comprimento = float(input(f'COMPRIMENTO (m): '))
area(largura, comprimento)


# %%
