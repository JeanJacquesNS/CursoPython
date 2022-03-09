s='Monty Python'
# imprime a string a partir da posicao "0" , mas nao inclui a posicao "4", se a posicao for maior que o tamanho da string ele
# assume a ultima posicao
print(s[0:4])
# pode se ocultar um dos elementos , no caso do primeiro ele assume a primeira posicao e no caso da ultima ele assume a ultima posicao
# Se for a ocultar os dois parametros, ele assume toda string
print(s[:2])
print(s[8:])
print(s[:])

# utilizando "in" como um operador logico
fruit='banana'
'n' in fruit
'm' in fruit
'nan' in fruit

if 'a' in fruit:
    print('Found it!')

# Livraria de string
great ='Hello Bob'
zap=great.lower()
print(zap)

print(great)
print('Hi There'.lower())

# Pesquisar e Subistituir
great= 'Hello Bob'
nstr=great.replace('Bob','Jane')
print(nstr)

nstr=great.replace('o','X')
print(nstr)

# Inserindo e Extraindo dados de uma string
data='Form stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos=data.find('@')
print(atpos)
sppos=data.find(' ',atpos)
print(sppos)
host=data[atpos+1:sppos]
print(host)

# Dois tipos de Strings
