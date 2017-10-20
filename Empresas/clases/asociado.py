from datetime import datetime

class asociados(object):
    cuit = 0
    nombre = ""
    fechaIngreso = datetime

    def getAntiguedad(self):
        return (self.fechaIngreso - datetime.now())