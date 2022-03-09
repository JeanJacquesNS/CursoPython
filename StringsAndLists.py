# "split" divide uma string em partes e produz uma lista de strings. podemos imaginar o resultado como palavras.
# Podemos aceder uma certa palavra or pesquisar em todas palavras.
abc='With three words'
stuff=abc.split()
print(stuff)

for w in stuff:
    print(w)

# quando nao especificas o "delimiter", multiplos espacos sao tratados como um delimiter
# podes especificar o que queres usar como delimiter no "split"
line='first,second,third'
thing=line.split()
print(thing)

thing=line.split(',')
print(thing)

# Padrao de split duplo
