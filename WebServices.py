#XML
#Documento XML
<person>
	<lastname>Severance</lastname>
	<age>17</age>
	<dateborn>2001-04-17</dateborn>
</person>

#Contrato de Schema XML  (Estrutura XSD)
<xs: complexType name="person">
	<xs:sequence>
		<xs:element name="lastname" type="xs:string" minOccurs = "1" maxOccurs="1"/>
		<xs:element name="age" type="xs:integer"/>
		<xs:element name="dateborn" type="xs:date"/>
	</xs:sequence>
</xs:complexType>

#Lendo um ficheiro XML recebido de fora
import xml.etree.ElementTree as ET

data= '''<person>
	<name>Chuck</name>
	<phone type = "intl">
	+1 734 303 4456
	</phone>
	<email hide="yes"/>
	</person>
'''

tree= ET.fromstring(data)
print('Name: ',tree.find('name').text)
print('Áttr: ',tree.find('email').get('hide'))


#JavaScript Object Notation (JSON)
import json

data ='''
		"name": "Chuck",
		"phone": {
			"type": "intl",
			"number": "+1 734 303 4456"
		},
		"email": {
			"hide": "yes"
		}
'''

#aqui e criado um dicionario com os dados json recebidos
info = json.loads(data)
print('Name:', infor["name"])


#Lista de Json
input ='''
	{	"id" : '001',
		"x" : "2",
		"name" : "Chuck"
	},
	{	"id" : '009',
		"x" : "7",
		"name" : "Chuck"
	}
'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
	print('Name', item['name'])
	print('Id', item['id'])
	print('Attribute',item['x'])
	
	
#Service Abordagem Orientada

#API (Application Program Interface)

#Ficheiro Json retornado pelo endereco: http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI

# {
#	"status": "OK",
#	"results": [
#			"geometry": {
#				"location_type": "APROXIMATE",
#				"location": {
#					"lat":42.2808256,
#					"lng": -83.7430378
#				}
#			},
#			"adress_components":[
#				{
#					"long_name": "Ann Arbor",
#					"types": [
#						"locality",
#						"political"
#					],
#					"short_name": "Ann Arbor"
#				}
#			],
#			"formatted_address": "Ann Arbor, MI, USA",
#			"types":[
#				"locality",
#				"politicaly"
#			]
#	]
# }
# 

import urllib.request, urllib.parse, urllib.error

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = input('Enter Location: ')
	if len(address)<1: break
	
	url =serceurl + urllib.parse.urlencode({'address': address})
	
	print('Retrieving', url)
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	print('Retrieved', len(data), 'characters')
	
	try:
		js = json.load(data)
	except:
		js= None
		
	if not js or 'status' not in js or js['status']!='OK':
		print('==== Failure to Retrieve ====')
		print(data)
		continue
	
	lat = js["results"][0]["geometry"]["location"]["lat"]
	lng = js["results"][0]["geometry"]["location"]["lng"]
	print('lat', lat, 'lng', lnng)
	location = js['results'][0]['formatted_address']
	print(location)

