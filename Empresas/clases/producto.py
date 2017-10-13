from .material import materiales

class productos(object):
    idProducto = 0
    Nombre = ""
    Coste = 0
    Descripcion = ""
    Categoria = ""
    material = []

    def setProducto(self,nombre,coste,descripcion,idCategoria):
        self.Nombre = nombre
        self.Coste = coste
        self.Descripcion = descripcion
        self.Categoria = idCategoria

    def AgregarMaterial(self,materiale):
        self.material.append(materiale)

