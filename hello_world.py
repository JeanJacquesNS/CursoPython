print("Hello Python world!")
name = "jean \tjacques \nn.s"
#title() coloca todas iniciais como maiusculas
print(name.title())
first_name="     Jean"
last_name="Shima      "
full_name=first_name+" "+last_name
print(full_name)
#strip() , lstrip() e rstrip() servem para remover espacos em brancos a direita e a esquerda
print(full_name.strip())
#print(full_name.lstrip())

#Python nao consegui diferencia numero e texo quando concantenados, entao, quando precisar 
#concantenar as duas coisas , tera que ser usado o str() para converter a variavel numerica em texto
age=28
message= "Happy "+str(age)+"rd Birthday!"
print(message)

import this
