class PartyAnimal:
	x =0
	name ="" 
	def party(self):
		self.x = self.x+1
		print(self.name,"party count",self.x)
		
	def __init__(self,z):
		self.name=z
		print(self.name, "construido ")
	
	#def __init__(self):
		#print("I am construido ")
		
	#def __del__(self):
		#print("Estou destruido ", self.x)
		
#an = PartyAnimal()

#an.party()
#an.party()
#an=42
#print('an contem ',an)

s = PartyAnimal("Sally")
s.party()

j=PartyAnimal("Jim")
j.party()
s.party()
print("============================================")

#Maneira Nerd de encontrar a capacidade
#print("Tipo: ",type(an))
#print("capacidade: ",dir(an))


#Ciclo de vida de um objecto

print("============================================")

#Heranca

#Criando um objecto que herda a classe PartyAnimal

class FootballFan (PartyAnimal):
	points =0
	
	def touchdown(self):
		self.points= self.points+7
		self.party()
		print(self.name, "points",self.points)


k= Football("Jean")
k.party()
k.touchdown()
