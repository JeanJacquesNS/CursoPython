#Tuplas sao outro tipo de sequencia que funciona muito mais como uma lista
#Elas tem elementos que sao indexadas iniciando do zero
x = ('Glenn', 'Sally','Joseph')
print(x[2])
y=(1,9,2)
print(y)
print(max(y))

#A diferenca entre tuplas elistas e que as tuplas sao imutaveis

#Tuplas e Dicionarios
d= dict()
d['csev'] = 2
d['cwen'] = 4

for (k,v) in d.items():
	print(k,v)

tups = d.items()
print(tups)

#Tuplas sao comparaveis
#A operacao de comparacao funciona com tuplas e outras sequencias. se o primeiro item e qual, python vai para o proximo elemento, e assim por diante, ate encontrar elementos diferentes.
(0,1,2)<(5,1,2)
