
'''
	Se comunica con arduino por el puerto serie

	Author 	: Jose Luis Noguera Dols
	Date	: 07/10/2018
'''
import serial,time

class ArduinoComunication(object):

    def __init__(self,puerto):
        self.nomApp = "as"
        self.puertoCom = puerto
        self.arduino = serial.Serial(puertoCom,9600)

    def Read():
        try:
            time.sleep(2)
            rawString = arduino.readline()
            arduino.close
            return rawString
        except e:
            raise Exception(self.nomApp+ e)
