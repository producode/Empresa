from .material import materiales
from datetime import datetime

class compras(object):
    Precio = 0
    idCompra = 0
    Fecha = datetime
    material = materiales
    cantidad = 0

    def agregarMaterial(self,materiale):
        self.material = materiale
