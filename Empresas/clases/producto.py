from .material import materiales
from .categoria import categorias

class productos(object):
    Nombre = ""
    Coste = 0
    Descripcion = ""
    Categoria = categorias
    material = []

    def setProducto(self,nombre,coste,descripcion,idCategoria):
        self.Nombre = nombre
        self.Coste = coste
        self.Descripcion = descripcion
        self.IdCategoria = idCategoria

    def AgregarMaterial(self,materiale):
        self.material.append(materiale)

