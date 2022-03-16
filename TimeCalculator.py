def add_time(param1,param2,param3='Monday'):
	
	timeframe=param1.split(' ')
	timeFrame2=timeframe.split(':')
	result=0
	
	if timeframe[1]=='AM':
		minutes= int(timeFrame2[1])+ int((param2.split(':'))[1])
		print(minutes)
	else:
