#Comparando e Extraindo Dados
#re.search() retorna um Verdadeiro/Falso dependendo do resultado da comparacao
#Se na verdade queremos que a comparacao da string seja extraido utilizamos re.findall()

import re
x='My 2 favorite numbers are 19 and 42'
#Se for a remover o sinal +, ele ira retornar os valores encontrados separados, mas se adicionar o +
#ira juntar os dados que se seguem
y= re.findall('[0-9]+',x)
print(y)
print("===========================================================")
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#retorna a posicao do @
atpos= data.find('@')
print(atpos)

sppos= data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print (host)
print("===========================================================")
#O split duplo
words =data.split()
email= words[1]
pieces = email.split('@')
print(pieces[1])

print("===========================================================")
#A Versao Regex
#[^ ] => Equipara non-blank character
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y=re.findall('From .*@([^ ]*)',lin)
print(y)

#hand = open('mbox-short.txt')
#numList = list()
#for line in hand:
#	line = line.rstrip()
#	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
#	if len(stuff)!=1: continue
#	num = float(stuff[0])
#	numlist.append(num)
#print ('Maximum:', max(numList))
