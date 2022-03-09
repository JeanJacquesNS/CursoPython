
#padrao de Contagem
counts =dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')

for word in words:
	counts[word]=counts.get(word,0)+1
print('Counts ', counts)

#Recuperando  lista de chaves e valores

#e possivel ter a lista de chaves, valores ou itens(ambos) do dicionario
jjj={'chuck':1,'fred':42,'jan':100}
#retorna a lista das chaves
print(list(jjj))
#retorna a lista das chaves
print(jjj.keys())
#retorna a lista dos valores contidos nas listas
print(jjj.values())
#retorna tuplas das chaves e seus respectivos valores
print(jjj.items())

#Variaveis de dupla iteracao
jj= {'chuck': 1,'fred':42,'jan':100}
for aaa,bbb in jjj.items():
	print(aaa,bbb)
