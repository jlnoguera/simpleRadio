'''
	Carga una lista de emisoras en una lista
	y permite escucharlas

	Author 	: Jose Luis Noguera Dols
	Date	: 27/08/2018 
'''

import vlcapi
import json

class Radio:

	'''
		Constructor sobrecargado
	'''
	def __init__(self):
		self.nomApp = "Radio->"

		self.mediaPlayer = None
		self.urlJson = None
		self.stationActual = 1
		self.stationLen = 0
		self.stationName = ""

		self.LoadList()

	'''
		Destructor
	'''
	def __del__(self):
		self.mediaPlayer = None		
		self.urlJson = None

	'''
		Carga el Json radioslist con las emisoras guardadas
	'''
	def LoadList(self):
		try:
			with open('radioslist.json') as datos:
				self.urlJson = json.load(datos)

			#obtengo cantiada de estaciones de radio
			datos = None	
			datos = json.dumps(self.urlJson)
			itemdict = json.loads(datos)
			self.stationLen = len(itemdict)

			print(self.urlJson)
		except Exception,e:
			raise Exception(e)

	'''
		Devuelve un json con las emisoras guardadas
	'''
	def Stations(self):
		return self.urlJson

	def StationPlay(self,orden):
		try:
			self.mediaPlayer = None
			self.stationActual = orden

		 	#	url = self.GetUrl(orden)
			item = None
			item = self.GetStationData(orden) 
			print("la url selecionada es : "+item["url"]+" con nombre "+item["nombre"])
			self.stationName = item["nombre"]

			self.mediaPlayer = vlcapi.VlcApi(item["url"])
			self.mediaPlayer.Play()
		except Exception,e:
			raise Exception(e)

	def GetStationData(self,orden):
		try:
			for item in self.urlJson:
				if item["orden"] == orden:
						return item 
			
		except Exception,e:
			raise Exception(e)			
		
	'''
		Reproduce una emisora de radio
	'''
	def Play(self):
		try:			
			self.mediaPlayer.Play()
		except Exception,e:
			raise Exception(e )

	'''
		Pone en pausa una emisora 
	'''
	def Pause(self):
		try:
			self.mediaPlayer.Pause()
		except Exception,e:
			raise Exception(e)

	'''
		Para la reproduccion de una emisora
	'''
	def Stop(self):
		try:			
			self.mediaPlayer.Stop()
		except Exception,e:
			raise Exception(e)

	def NextStation(self):
		try:
			if (self.stationActual == self.stationLen):
				self.stationActual = 1
				self.StationPlay(self.stationActual)
			else:
				self.stationActual = self.stationActual+1
				self.StationPlay(self.stationActual)
		except Exception,e:
			raise Exception(e)
		
	def PrevStation(self):
		try:
			if (self.stationActual == 1):
				self.stationActual = self.stationLen
			else:
				self.stationActual = self.stationActual-1
		except Exception,e:
			raise Exception(e)

