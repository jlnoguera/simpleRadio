import radio
import time
'''
    Recoge las acciones realizadas en Arduino para pedirselas a la Radio

    Author  : Jose Luis Noguera Dols
    Date    : 28/08/18
'''
class InterfaceRadioArduino:

    def __init__(self):
        self.nomApp = "InterfaceRadioArduino->"
        self.radio = radio.Radio()

    def __del__(self):
        self.radio = None

    def Play(self,orden):
        try:
            self.radio.StationPlay(orden)
        except Exception,e:
            raise Exception(self.nomApp+"Play : "+e)

    def Stop(self):
        try:
            self.radio.Stop()
        except Exception,e:
            raise Exception(self.nomApp+"Stop : "+e)
    
    def Pause(self):
        try:
            self.radio.Pause()
        except Exception,e:
            raise Exception(self.nomApp+e)

    def Next(self):
        try:
            self.radio.NextStation()
        except Exception,e:
            raise Exception(self.nomApp+e)

    def Prev(self):
        try:
            self.radio.PrevStation()
        except Exception,e:
            raise Exception(self.nomApp+e)


