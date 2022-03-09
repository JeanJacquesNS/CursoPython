#Criando uma lista e exibindo a mesma
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)

#Acessando elementos de uma lista
print(bicycles[2])

#Imprimindo um elemento da lista com iniciais maiusculas
print(bicycles[1].title())

#acedendo o ultimo elemento da lista
print(bicycles[-1])
#usando valores individuais de uma lista
message="My first bicylce was a "+bicycles[0].title()+"."
print(message)


#Alterando, acrescentando e removendo elementos
#Modificando elementos de uma lista
motorcycles=['honda','yamaha','suzuki']

motorcycles[0]='ducati'
print(motorcycles)

#Acrescentando elementos em uma lista
#Concantenando elementos no final de uma lista

motorcycles.append('jeep')
print(motorcycles)

#inserindo um elemento na lista e em uma determinada posicao
motorcycles.insert(0, 'BMW')
print(motorcycles)

#Removendo elementos de uma lista
#removendo um item usando a instrucao del
del motorcycles[1]
print(motorcycles)

#removendo com o  metodo pop(), este metodo remove o ultimo elemento da lista e permite que ainda seja utilizado
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#removendo itens de qualquer posicao em uma lista
first_owned=motorcycles.pop(0)
print("my first motorcycle was a "+first_owned)

#removendo de acordo com o nome
motorcycles.remove('suzuki')
print(motorcycles)

#Ordenando uma lista de forma permanente com o metodo sort()
bicycles.sort()
print(bicycles)

#ordenar de forma reversa
bicycles.sort(reverse=True)
print(bicycles)

# tamanho de uma lista
print('O tamanho da lista e: ',len(bicycles))

# utilizando a funcao "range"
print(range(len(bicycles)))
