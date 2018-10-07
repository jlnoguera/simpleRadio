import radio,arduinoComunication

'''
    Recoge las acciones realizadas en Arduino para pedirselas a la Radio
    Se realiza un bucle continuo leyendo del puerto serie de arduino

    Author  : Jose Luis Noguera Dols
    Date    : 07/10/18
'''
class InterfaceRadioArduino():

    def __init__(self,puerto):
        self.nomApp = "InterfaceRadioArduino->"
        self.radio = radio.Radio()
        self.arduino = arduinoComunication.ArduinoComunication(self,puerto)
        #Cambiando esta variable a true, se deja de comunicar con arduino
        self.stop = false
        #Recoge la opcion enviada por arduino, por defecto es cero (vacio)
        self.opcion = 0
        print("InterfaceRadioArduino")

    def LeerArduino(self):
        while self.stop==false:
            self.opcion = int(arduino.Read())
            if self.opcion > 0:
                RadioOpcion(self)

    def Stop(self):
        self.stop = true

    def RadioOpcion(self):
        self.Radio.StationPlay(self,self.opcion)
