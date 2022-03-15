def arithmetic_arranger (problems, calculate):
	numeradores=' '
	bases=' '
	linhas=' '
	result = ' '
	padding = ' '
	
	numberOfProblems=len(problems)
	arranged_problems = ''
	if numberOfProblems<=5:
		for problem in problems:
			splited= problem.split(' ')
			arranged= splited
			if arranged[1] in ['*','/']:
				arranged_problems = 'Error: Operator must be + or -.'		
				break
			else:
				if arranged[0].isdigit() and arranged[2].isdigit():
					if len(arranged[0])<=4 and len(arranged[2])<=4:	
						x=arranged[2]
						arranged[2]= x.rjust(8,padding)
						
						y=arranged[0]
						arranged[0]= y.rjust(9,padding)
						
						for i in range (1):
							linhas+=('{:'+'-'+'>'+str(9)+'}').format('')+"    "
						if calculate :
							z=0
							if arranged[1] == '+':
								z= int(arranged[0])+int(arranged[2])
							else:
								z = int (arranged[0]) - int(arranged[2])
							result += (str(z)).rjust(9,padding)+"    "
						numeradores+=str(arranged[0])+"    "
						bases+=arranged[1]+arranged[2]+"    "
					else:
						arranged_problems = 'Error: Numbers cannot be more than four digits.'
						break
				else:
					arranged_problems= 'Error: Numbers must only contain digits.'
					break
	else:
		arranged_problems = 'Error: Too many problems.'
		
	if arranged_problems == '':
		arranged_problems = numeradores.rstrip()+"\n"+bases+"\n"+linhas+"\n"+result

		
	return arranged_problems
	
