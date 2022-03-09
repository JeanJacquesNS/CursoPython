# percorendo um ficheiro em python para linha por linha de um ficheiro
fhand=open('sqrt.txt')
count =0
for line in fhand:
    count=count+1
print('Line Count:',count)

# Lendo todo ficheiro e armazenando os dados em uma unica string
fhand=open('sqrt.txt')
inp=fhand.read()
print(len(inp))
print(inp[:20])

# Fazendo uma pesquisa em um ficheiro
fhand=open('sqrt.txt')
for line in fhand:
    # removendo o espaco em branco que e impresso ao serem exibidas as impressoes
    line= line.rstrip()
    if line.startswith('From:'):
        print(line)
# saltando dados que nao queremos utilizando o ""continue""
fhand = open('sqrt.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# Utilizando "in" para selecionar linhas
fhand = open('sqrt.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

# Lendo ficheiros, atravez do nome (do ficheiro) e sua extensao introduzidos pelo utilizador
fname= input('Enter the file name: ')
fhand=open(fname)
count =0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were',count,'subject lines in', fname)

# Nomes incorrectos de ficheiros
fname=  input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened:',fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were',count,'subject lines in',fname)
