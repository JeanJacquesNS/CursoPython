import socket
#inicializacao do objecto que realiza a conexao, sem dados da conexao
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Fazendo a conexao
mysock.connect(('data.pr4e.org',80))
