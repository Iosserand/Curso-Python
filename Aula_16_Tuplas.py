#%%
lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')


for arnaldo in enumerate(lanche):
    comida = arnaldo[1]
    pos = arnaldo[0]
    print(pos, comida)
# %%


for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')



# %%
for comida in lanche:
    print(f'Eu vou comer {comida}')
# %%

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a 
print(c)
print(c.count(2))
print(c.index(4))
# %%
pessoa = ('Iosserand', 16, 'M', 75)
del (pessoa)
print(pessoa)
# %%
print(sorted(lanche))
# %%
