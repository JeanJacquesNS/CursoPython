def arithmetic_arranger (problems):
	lista=""
	numeradores=' '
	bases=' '
	linhas=' '
	
	padding = ' '
	t = 8
	for problem in problems:
		splited= problem.split(' ')
		arranged= splited
		tamanho=0
		x=arranged[2]
		arranged[2]= x.rjust(8,padding)
		
		y=arranged[0]
		arranged[0]= y.rjust(9,padding)
		
		for i in range (1):
			linhas+=('{:'+'-'+'>'+str(9)+'}').format('')+"  "
			
		numeradores+=str(arranged[0])+"  "
		bases+=arranged[1]+arranged[2]+"  "
		
	return numeradores.rstrip()+"\n"+bases+"\n"+linhas
	
