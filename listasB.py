# Concantenando listas utilizando "+"
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
# Criando uma lista vazia e atribuindo valores depois de declarar
stuff= list()
stuff.append('book')
stuff.append(99)
print(stuff)

# verificando se existe certo elemento na lista
some=[1,9,21,10,16]
# retorna False
9 in some
# retorna True
20 not in some

# organizando a lista utilizando o "sort"
friends=['Joseph','Glen','Sally']
friends.sort()
print(friends)

# Funcoes Builtin do python
nums=[3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
