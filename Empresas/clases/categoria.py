class categorias(object):
    nombre = ""
    idCategoria = 0

    def setCategoria(self,nombre,idCategoria):
        self.nombre = nombre
        self.idCategoria = idCategoria

    def getNombre(self):
        return self.nombre
    def getIdCategoria(self):
        return self.idCategoria