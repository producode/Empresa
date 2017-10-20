from .empleado import empleados
from .accionista import accionistas
from .pedido import pedidos
from .compra import compras
from .compania import companias
from .producto import productos
from datetime import datetime

class empresas(companias):
    Empleados = []
    Ahorros = 0
    accionistas = []
    Pedidos = []
    gananciaMensual = []
    Compras = []
    Productos = []

    def setEmpresa(self,nombre,rublo,abreviatura):
        self.Nombre = nombre
        self.Rublo = rublo
        self.Abreviatura = abreviatura

    def agregarEmpleado(self,dipendente):
        self.Empleados.append(dipendente)

    def agregarAccionista(self,azionista):
        self.accionistas.append(azionista)

    def agregarPedido(self,prodotto):
        pedidoNuevo = pedidos()
        for item in prodotto:
            pedidoNuevo.agregarProducto(item)
        pedidoNuevo.idPedido = len(self.Pedidos) + 1
        pedidoNuevo.Fecha = datetime.now()
        pedidoNuevo.precio = pedidoNuevo.getPrecio()
        self.Pedidos.append(pedidoNuevo)

    def eliminarPedido(self,ids):
        i = 0
        for o in self.Pedidos:
            if o.idPedido == ids:
                del self.Pedidos[i]
                break
            i = i + 1
    def eliminarEmpleado(self,cuit):
        i = 0
        for o in self.Empleados:
            if o.cuit == cuit:
                del self.Empleados[i]
                break
            i = i + 1

    def eliminarAccionista(self,cuit):
        i = 0
        for o in self.accionistas:
            if o.cuit == cuit:
                del self.accionistas[i]
                break
            i = i + 1
    def modificarAcciones(self,cuit,cantidad):
        i = 0
        for o in self.accionistas:
            if o.cuit == cuit:
                self.accionistas[i].cantidadAcciones = cantidad
                break
            i = i + 1


    def calcularGananciaMensual(self):  #calcula la ganancia de la empresa en el mes actual tomando como parametros
        sueldosMes = 0                  #los sueldos de los empleados existentes en el momento (gastos) y los
        for item in self.Empleados:     #pedidos realizados a la empresa en el mes actual (ganancias)
            sueldosMes = sueldosMes + item.sueldo
        gananciaMes = 0
        hoy = datetime.now()
        for item in self.Pedidos:
            if item.Fecha.month == hoy.month and item.Fecha.year == hoy.year:
                gananciaMes = gananciaMes + item.precio
        self.gananciaMensual.append(gananciaMes-sueldosMes)
        return gananciaMes - sueldosMes

    def calcularAhorros(self):               #calcula los ahorros segun la ganacia de todos los meses (es decir del
        self.Ahorros = 0                     #historial d ganancias mensuales) y luego les resta los gastos en compras
        for item in self.gananciaMensual:    #dando como resultado los ahorros que deberia tener la empresa
            self.Ahorros = self.Ahorros + item
        for item in self.Compras:
            self.Ahorros = self.Ahorros - item.Precio
        return self.Ahorros

    def agregarCompra(self,acquisto):
        self.Compras.append(acquisto)

    def obtenerIdCompra(self):
        return (len(self.Compras) + 1)

    def obtenerIdPedido(self):
        return (len(self.Productos) + 1)

    def getHistorialGanancia(self):
        return self.gananciaMensual

    def calcularCantidadAcciones(self):         #calcula la cantidad de acciones existentes hasta el momento
        total = 0
        for item in self.accionistas:
            total = total + item.cantidadAcciones
        return total

    def calcularDividendoAccion(self):          #calcula el dividendo de cada accionista. Esta predeterminado para que
        UP = len(self.gananciaMensual)          #los calcule de forma trimestral pero sin saber cuando fue el ultimo calculo
        if UP > 2:                              #para hacerlo utiliza las ganancias de los ultimos 3 meses (si existen)
            totalG = self.gananciaMensual[UP] + self.gananciaMensual[UP-1] + self.gananciaMensual[UP-2]
        return (totalG/self.calcularCantidadAcciones())

    def calcularDividendoAccionista(self):      #calcula el dividendo de cada accionista
        lista = []
        for item in self.accionistas:
            lista.append(item.cantidadAcciones * self.calcularDividendoAccion())
        return lista

    def calcularPorcentajeAccionista(self):     #calcula el porcentaje de acciones que posee cada accionista
        listaPorcentaje = []
        for item in self.accionistas:
            listaPorcentaje.append((100/self.calcularCantidadAcciones())*item.cantidadAcciones)
        return listaPorcentaje