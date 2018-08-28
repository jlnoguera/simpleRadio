'''
	Clase para el manejo de los metodos
	de la api de Vlc

	Author 	: Jose Luis Noguera Dols
	Date	: 27/08/2018
'''

import vlc

class VlcApi:

	def __init__(self,url):
		self.player = vlc.MediaPlayer(url) 

	def Play(self):
		self.player.play()

	def Pause(self):
		self.player.pause()

	def Stop(self):
		self.player.stop()
