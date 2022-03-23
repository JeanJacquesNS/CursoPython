param1='11:45 PM'
param2='1:00'
param3='Monday'
	
timeframe=param1.split(' ')

for time in timeframe:
	timeFrame2=time.split(':')
	break
result=0
pad='0'

print(timeframe[1],'e issso')

if str(timeframe[1]) == "PM":
	minutes= int(timeFrame2[1])+ int((param2.split(':'))[1])
	if minutes>=60:
		parteInteira= minutes/60
		resto=minutes%60
		if resto!=0:
			horas = int(timeFrame2[0])+int((param2.split(':'))[0])+int(parteInteira)
			if(horas<12):
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" PM")
			elif horas>=12:
				horas=int(horas/12)
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" AM")
		else:
			horas = int(timeFrame2[0])+int((param2.split(':'))[0])+int(parteInteira)
			if(horas<12):
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" PM")
			elif horas>=12:
				horas=int(horas/12)
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" AM")
					
	else:
		horas = int(timeFrame2[0])+int((param2.split(':'))[0])
		if horas>=12:
			parteInteiraH= int(horas/12)
			restoH= horas%12
			horas= parteInteiraH	
			print(str(restoH).rjust(2,pad)+":"+ str(minutes).rjust(2,pad) +" AM")
		else:
			print(str(horas).rjust(2,pad)+":"+ str(minutes).rjust(2,pad) +" AM")
	print(minutes)
else:
	minutes= int(timeFrame2[1])+ int((param2.split(':'))[1])
	if minutes>=60:
		parteInteira= minutes/60
		resto=minutes%60
		if resto!=0:
			horas = int(timeFrame2[0])+int((param2.split(':'))[0])+int(parteInteira)
			if(horas<12):
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" AM")
			elif horas>=12 and horas<13:
				horas=int(horas/12)
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" AM")
			elif horas>=13:
				horas=int(horas/12)
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" PM")
				
		else:
			horas = int(timeFrame2[0])+int((param2.split(':'))[0])+int(parteInteira)
			if(horas<12):
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" AM")
			elif horas>=12 and horas<13:
				horas=int(horas/12)
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" AM")
			elif horas>=13:
				horas=int(horas/12)
				print(str(horas).rjust(2,pad)+":"+str(resto).rjust(2,pad)+" PM")
							
	else:
		horas = int(timeFrame2[0])+int((param2.split(':'))[0])
		if horas>=13 and horas < 14:
			parteInteiraH= int(horas/12)
			restoH= horas%12
			horas= parteInteiraH	
			print(str(horas).rjust(2,pad)+":"+ str(minutes).rjust(2,pad) +" PM")
		elif horas>=14:
			parteInteiraH= int(horas/12)
			restoH= horas%12
			horas= restoH	
			print(str(horas).rjust(2,pad)+":"+ str(minutes).rjust(2,pad) +" PM")
	
	print(minutes)
	print('Yeah')
	minutes= int(timeFrame2[1])+ int((param2.split(':'))[1])
	print(minutes)

