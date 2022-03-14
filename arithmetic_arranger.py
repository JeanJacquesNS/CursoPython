def arithmetic_arranger (problems):
	lista=""
	for problem in problems:
		splited= problem.split("+")
		arranged= splited
		print(arranged[0],"\n","+",arranged[1])
		print("====================================")
		linha=""
		tamanho=0
		if len(arranged[0])>len(arranged[1]):
			for i in range(0,(len(arranged[0])-len(arranged[1]))+4):
				x=" ";
				arranged[1]=x+arranged[1]
			tamanho=len(arranged[1])
		else:		
				for i in range(0,(len(arranged[1])-len(arranged[0]))+4):
					x=" ";
					arranged[0]=x+arranged[0]
				tamanho=len(arranged[0])
		for i in range (2,tamanho):
			linha+="-"
		print(str(arranged[0]),"\n","+",str(arranged[1]),"\n",linha," ")
		
	list= (lista.rstrip()).split("")
	return list
	
