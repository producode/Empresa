from .material import materiales
from .compania import companias

class fabricantes(companias):
    materiale = []

    def crearMaterial(self,nombre,precio,unidad):
        materialNuevo = materiales()
        materialNuevo.Nombre = nombre
        materialNuevo.Precio = precio
        materialNuevo.UnidadMedicion = unidad
        self.materiale.append(materialNuevo)

    def borrarMaterial(self,nombre):
        i = 0
        for o in self.materiale:
            if o.Nombre == nombre:
                del self.materiale[i]
                break
            i = i + 1