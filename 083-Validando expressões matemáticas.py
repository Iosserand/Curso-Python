#%%

expressao = str('(a+b)*c+((a+b+c))*x')
# expressao = str('(a+b)*c+((a+b+c)*x')
print(len(expressao))
primeiro_corte = expressao.split('(')
segundo_corte = expressao.split(')')


if  (len(primeiro_corte)-1) == (len(segundo_corte)-1):
    print('Sua expresão está válida')
else:
    print('Sua expresão está errada')



# %%
expressao = str('(a+b)*c+((a+b+c))*x')
cont = 0
for elemento in expressao:
    if elemento == '(':
        cont += 1
    elif elemento == ')':
        cont -= 1
    if cont < 0:
        print('Sua expresão está errada')
        break
# print(cont)
if cont == 0:
    print('Sua expresão está válida')
elif cont > 0:
    print('Sua expresão está errada')


        


    
# %%
