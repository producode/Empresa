from .producto import productos
from datetime import datetime

class pedidos(object):
    idPedido = 0
    precio = 0
    prodotto = []
    Fecha = datetime

    def getPrecio(self):
        total = 0
        for item in self.prodotto:
            total = total + item.getCoste()
        self.precio = total
        return total

    def agregarProducto(self,produrre):
        self.prodotto.append(produrre)



