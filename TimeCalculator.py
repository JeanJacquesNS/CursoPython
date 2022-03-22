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
		print(str(horas).rjust(2,pad)+":"+ str(minutes).rjust(2,pad) +" PM")
	print(minutes)
else:
	print('Yeah')
	minutes= int(timeFrame2[1])+ int((param2.split(':'))[1])
	print(minutes)

