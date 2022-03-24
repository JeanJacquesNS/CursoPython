param1='11:43 PM'
param2='24:20'
param3='Tuesday'
pad='0'
pm="PM"
am="AM"
diaSemana=""
daysOfWeek = {'Sunday':1,'Monday':2,'Tuesday':3,'Wednesday':4,'Thursday':5,'Friday':6,'Saturday':7}

def somarHoras(horas1,horas2):
	return int(horas1)+int(horas2)
	
def somarMinutos(minutos1,minutos2):
	return int(minutos1)+int(minutos2)
	
def parteInteiraMinutos(minutos):
	return int(minutos/60)
	
def restoDivisaoMinutos(minutos):
	return minutos%60
	
def parteInteiraHoras(horas):
	return	int(horas/12)

def restoDivisaoHoras(horas):
	return horas%12
	
def diaSemana(horas,diaDaSemana="None"):
	horas= (int(horas)%24)%12
	dias=round((horas/24))
	diaSemana=""
	if diaDaSemana != "None":
		for key1,value1 in daysOfWeek.items():
			if key1 == diaDaSemana:
				for key2,value2 in daysOfWeek.items():
					if ((dias-value1)*(-1)) == value2:
						if (dias-value1)== 0:
							diaSemana += " "+key1
						else:
							diaSemana += " "+key2
					
	return diaSemana
	
def dias(horas,diaSemana="None"):
	tempo=""
	horas= (int(horas)%24)%12
	dias=round((horas/24))
	print(dias)
	if dias<=1 and diaSemana=="None":
		tempo= " (next day)"
	elif dias > 1 and diaSemana!="None":
		tempo = dias+" days later"
	return tempo
	
timeframe = param1.split(' ')

for time in timeframe:
	timeFrame2=time.split(':')
	break
if param3!='':
	diass=''

if str(timeframe[1]) == pm:
	minutes = somarMinutos(timeFrame2[1],(param2.split(':'))[1])
	if minutes >= 60:
		parteInteira = parteInteiraMinutos(minutes)
		resto = restoDivisaoMinutos(minutes)
		if resto!=0:
			horas = somarHoras(timeFrame2[0],(param2.split(':'))[0]) + parteInteira
			horassomadas = horas
			if horas <= 12 and horas < 13:
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" "+pm)
			elif horas >= 13 and horas <24:
				horas = parteInteiraHoras(horas)
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" "+am+dias(horassomadas))
			elif horas>24:
				hora = parteInteiraHoras(horas)
				rest = restoDivisaoHoras(horas)
				if rest == 0:
					rest=12
				print(str(rest).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" "+am+diaSemana(horas,param3)+ dias(horas,param3))
				
		else:
			horas = somarHoras(timeFrame2[0],(param2.split(':'))[0]) + parteInteira
			if(horas<12):
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" "+pm)
			elif horas >= 12:
				horas=parteInteiraHoras(horas)
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" "+am)				
	else:
		horas = somarHoras(timeFrame2[0],(param2.split(':'))[0])
		if horas >= 12:
			parteInteiraH = parteInteiraHoras(horas)
			restoH = restoDivisaoHoras(horas)
			#horas = parteInteiraH	
			print(str(restoH).rjust(2,pad)+":"+ str(minutes).rjust(2,pad) +" "+am+" "+dias(horas))
		else:
			print(str(horas).rjust(2,pad)+":"+ str(minutes).rjust(2,pad) +" "+pm)
else:
	minutes = somarMinutos(timeFrame2[1],(param2.split(':'))[1])
	if minutes >= 60:
		parteInteira = parteInteiraMinutos(minutes)
		resto= restoDivisaoMinutos(minutes)
		if resto!=0:
			horas = somarHoras(timeFrame2[0],(param2.split(':'))[0]) + parteInteira
			if(horas<12):
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" "+am)
			elif horas>=12 and horas<13:
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" "+pm)
			elif horas>=13:
				hora=parteInteiraHoras(horas)+1
				print(str(hora).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" "+ pm + diaSemana(horas,param3))
				
		else:
			horas = somarHoras(timeFrame2[0],(param2.split(':'))[0]) + parteInteira
			if(horas<12):
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" "+am)
			elif horas>=12 and horas<13:
				horas=parteInteiraHoras(horas)
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" "+am)
			elif horas>=13:
				horas = parteInteiraHoras(horas)+1
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" "+pm+diaSemana(horas,param3))
							
	else:
		horas = somarHoras(timeFrame2[0],(param2.split(':'))[0]) + parteInteira
		if horas>=13 and horas < 14:
			parteInteiraH= parteInteiraHoras(horas)
			restoH= restoDivisaoHoras(horas)
			horas= parteInteiraH	
			print(str(horas).rjust(2,pad)+":"+ str(minutes).rjust(2,pad) +" "+pm)
		elif horas>=14:
			parteInteiraH= parteInteiraHoras(horas)
			restoH= restoDivisaoHoras(horas)
			horas= restoH	
			print(str(horas).rjust(2,pad)+":"+ str(minutes).rjust(2,pad) +" "+pm)
	
