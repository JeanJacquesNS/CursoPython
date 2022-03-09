# Dicionarios em python nao tem ordem logica
# permitem simular operacoes de base de dados de forma rapida
# por nao ter ordem logica de entrada, indexamos as coisas que colocamos no tal dicionario com um "lookup tag"

purse=dict()
purse['money']=12
purse['candy']=3
purse['tissues']=75
print(purse)
print(purse['candy'])

purse['candy']=purse['candy']+2
print(purse)

# Unica diferenca entre listas e dicionarios e que nas listas os indexs sao em ordem de entrada enquanto que nos
# dicionarios nos e que informamos os index

# Dicionarios Literais (Constantes)
jjj={'chuck':1,'fred':42,'jan':100}
print(jjj)
ooo={}
print(ooo)

#O metodo "get" para dicionarios

#o padrao de verificar se uma chave ja esta no dicionario e assumir um valor se a chave nao estiver la, e tao comum que haja um metodo chamado get() que faz isso por nos

if name in names:
	x=names[name]
else:
	x=0
	
x=counts.get(name,0)


#Conta simplificada com get()

#podemos utilizar get() e prover um valor padrao 0 quando a chave nao estiver no dicionario e depois so adicionar um

counts = dict()

names= ['csev','cwen','csev','zqian','cwen']

for name in names :
	counts[name]= counts.get(name,0)+1
print(counts)
