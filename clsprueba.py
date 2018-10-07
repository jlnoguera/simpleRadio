import ifRadioArduino

class prueba(object):

    def __init__(self):

        ra = ifRadioArduino.InterfaceRadioArduino(self,"com3")
        ra.LeerArduino(self)
