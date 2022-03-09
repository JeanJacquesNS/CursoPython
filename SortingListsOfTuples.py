d = {'a':10,'b':1,'c':22}
d.items()
print(d.items())
print(sorted(d.items()))
print('======================================================')

#Sorteando pelos valores ao inves de chave

c = {'a':10,'b':1,'c':22}
tmp = list()
for k,v in c.items():
	tmp.append((v,k))
	
print(tmp)

tmp = sorted(tmp,reverse = True)
print(tmp)


#Lendo ficheiro, contando o numero de vezes que uma palavra e repetida e guardando a chave e o valor num dicionario
#criando uma lista de tuplas dos items do dicionario, sorteando em ordem reversa os elementos da lista, e por fim,
#ler as chaves e seus valores na lista (imprimindo a chave e depois o valor), partindo do 11 registo na lista


fhand= open('romeo.txt')
counts=dict()

for line in fhand:
	words=line.split()
	for word in words:
		counts[word]= counts.get(word,0)+1

lst= list()
for key, val in counts.items():
	newtup = (val,key)
	lst.append(newtup)

lst = sorted(lst,reverse=True)

for val,key in lst(:10):
	print(key,val)

#versao mais curta
c = {'a':10,'b':1,'c':22}
print(sorted([(v,k)for k,v in c.items()]))

#compreensao desta lista: cria uma lista dinamica. nesse caso, criamos um lista de tuplas inversas e depois sorteamos a lista
