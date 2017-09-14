from .asociado import asociados

class accionistas(asociados):
    cantidadAcciones = 0

    def setAcciones(self,numero):
        self.cantidadAcciones = numero