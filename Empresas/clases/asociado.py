from datetime import datetime

class asociados(object):
    nombre = ""
    fechaIngreso = datetime

    def getAntiguedad(self):
        return (self.fechaIngreso - datetime.now())