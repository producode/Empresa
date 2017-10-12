from datetime import datetime
from datetime import date
from Empresas.clases.empresa import empresas
from Empresas.clases.fabricante import fabricantes
from Empresas.clases.categoria import categorias
from Empresas.clases.empleado import empleados
from Empresas.clases.accionista import accionistas
from Empresas.clases.compra import compras
from Empresas.clases.usuario import usuarios
from flask import Flask
from flask import render_template
from flask import request

empresa = []
fabbricantes = []
categoriaLista = []
cliente = []
abrUniversal = "eds"
fabUniversal = "aaa"

def ingresarEmpresa2(nombre,rublo,abreviatura):
    nuevaEmpresa = empresas()
    nuevaEmpresa.Nombre = nombre
    nuevaEmpresa.Rublo = rublo
    nuevaEmpresa.Abreviatura = abreviatura
    empresa.append(nuevaEmpresa)
def ingresar2(nickname,password):
    for item in cliente:
        if(nickname == item.nickname and password == item.contrasena):
            abrUniversal = item.empresaAsociada
def registrarse2(nickname,password,empresasociada):
    nuevoUsuario = usuarios()
    nuevoUsuario.nickname = nickname
    nuevoUsuario.contrasena = password
    nuevoUsuario.empresaAsociada = empresasociada
    cliente.append(nuevoUsuario)
def ingresarEmpleado2(nombre,profesion,superior,sueldo):
    i = 0
    a = False
    for o in empresa:
        if o.Abreviatura == abrUniversal:
            a = True
            break
        i = i + 1
    if a == True:
        nuevoEmpleado = empleados()
        nuevoEmpleado.nombre = nombre
        nuevoEmpleado.fechaIngreso = datetime.now()
        nuevoEmpleado.Profesion = profesion
        nuevoEmpleado.superior = superior
        nuevoEmpleado.sueldo = sueldo
        empresa[i].agregarEmpleado(nuevoEmpleado)
def ingresarAccionista2(nombre,cantidad):
    i = 0
    a = False
    for o in empresa:
        if o.Abreviatura == abrUniversal:
            a = True
            break
        i = i + 1
    if a == True:
        nuevoAccionista = accionistas()
        nuevoAccionista.nombre = nombre
        nuevoAccionista.fechaIngreso = datetime.now()
        nuevoAccionista.cantidadAcciones = cantidad
        empresa[i].agregarAccionista(nuevoAccionista)
def listarEmpleados2(): #busca el numero de la empresa segun el abrUniversal, por lo que se puede usar para cualquier cosa que lo requiera.
    a = False
    i = 0
    for o in empresa:
        if o.Abreviatura == abrUniversal:
            a = True
            break
        i = i + 1
    if a:
        return i
    else:
        return 0
def modifcarEmpleado2(nombre,superior,sueldo):
    for o in empresa[listarEmpleados2()].Empleados:
        if o.nombre == nombre:
            o.superior = superior
            o.sueldo = sueldo
            break
def eliminarEmpleado2(nombre):
    empresa[listarEmpleados2()].eliminarEmpleado(nombre)
def modificarAccionista2(nombre,cantidad):
    empresa[listarEmpleados2()].modificarAcciones(nombre, cantidad)
def eliminarAccionista2(nombre):
    empresa[listarEmpleados2()].eliminarAccionista(nombre)
def elegirFabricane(fabricante):
    i = 0
    for o in fabbricantes:
        if o.Abreviatura == fabricante:
            break
        i = i + 1
    return i
def insertarCompra2(fabricante,material,cantidad):
    nuevaCompra = compras()
    nuevaCompra.idCompra = empresa[listarEmpleados2()].obtenerIdCompra()
    nuevaCompra.Fecha = datetime.now()
    for item2 in fabbricantes[elegirFabricane(fabricante)].materiale:
        if item2.Nombre == material:
            nuevaCompra.material = item2
            nuevaCompra.cantidad = int(cantidad)
            nuevaCompra.Precio = (nuevaCompra.cantidad * nuevaCompra.material.Precio)
            empresa[listarEmpleados2()].agregarCompra(nuevaCompra)
def listarMateriales2(fabricante):

app = Flask(__name__)
@app.route('/')
@app.route('/inicio', methods=['GET', 'POST'])
def inicio():
    return render_template('inicio.html')
@app.route('/')
@app.route('/principal', methods=['GET', 'POST'])
def principal():
    return render_template('principal.html')
@app.route('/')
@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
        ingresar2(request.form['nicknameUsuario'],request.form['password'])
    return render_template('ingreso.html')
@app.route('/')
@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        registrarse2(request.form['nicknameUsuario'],request.form['password'],request.form['abreviatura'])
    return render_template('registrarse.html')
@app.route('/')
@app.route('/finanzasMenu', methods=['GET', 'POST'])
def finanzasMenu():
    return render_template('FinanzasMenu.html')
@app.route('/')
@app.route('/empresasMenu', methods=['GET', 'POST'])
def empresasMenu():
    return render_template('EmpresasMenu.html')
@app.route('/')
@app.route('/comprasMenu', methods=['GET', 'POST'])
def comprasMenu():
    return render_template('ComprasMenu.html')
@app.route('/')
@app.route('/materialesMenu', methods=['GET', 'POST'])
def materialesMenu():
    return render_template('MaterialesMenu.html')
@app.route('/')
@app.route('/productosMenu', methods=['GET', 'POST'])
def productosMenu():
    return render_template('ProductosMenu.html')
@app.route('/')
@app.route('/pedidosMenu', methods=['GET', 'POST'])
def pedidosMenu():
    return render_template('PedidosMenu.html')
@app.route('/')
@app.route('/ingresarEmpresa', methods=['GET', 'POST'])
def ingresarEmpresa():
    if request.method == 'POST':
        ingresarEmpresa2(request.form['empresaNombre'],request.form['empresaRublo'],request.form['empresaAbreviatura'])
    return render_template('AgregarEmpresa.html',
                           title='Sign In')
@app.route('/')
@app.route('/listarEmpresas', methods=['GET','POST'])
def listarEmpresas():
    return render_template("listarEmpresas.html",
                           title='Home',
                           posts=empresa)
@app.route('/')
@app.route('/listarFabricantes', methods=['GET','POST'])
def listarFabricantes():
    return render_template("listarFabricantes.html",
                           title='Home',
                           posts=fabbricantes)
@app.route('/')
@app.route('/listarEmpleados', methods=['GET','POST'])
def listarEmpleados():
    return render_template("listarEmpleados.html",
                           title='Home',
                           posts=empresa[listarEmpleados2()].Empleados)
@app.route('/')
@app.route('/listarAccionistas', methods=['GET','POST'])
def listarAccionistas():
    return render_template("listarAccionistas.html",
                           title='Home',
                           posts=empresa[listarEmpleados2()].accionistas)
@app.route('/')
@app.route('/listarCompras', methods=['GET','POST'])
def listarComprass():
    return render_template("listarCompras.html",
                           title='Home',
                           posts=empresa[listarEmpleados2()].Compras)
@app.route('/')
@app.route('/ingresarEmpleado')
def agregarEmpleado():
    if request.method == 'POST':
        nombre = request.form['nombre']
        profesion = request.form['profesion']
        superior = request.form['superior']
        sueldo = request.form['sueldo']
        ingresarEmpleado2(nombre,profesion, superior,sueldo)
    return render_template("ingresarEmpleado.html")
@app.route('/')
@app.route('/verFabricante')
def verFabricante():
    if request.method == 'POST':
        fabUniversal = request.form['abreviatura']
    return render_template("verFabricante.html")
app.run(debug=True)

print("--Bienvenido--")
print("")
seguir = True
while seguir:
    print("elija una opcion")
    print("1: FINANZAS")
    print("2: EMPRESAS")
    print("3: COMPRAS")
    print("4: MATERIALES")
    print("5: PRODUCTOS")
    print("6: PEDIDOS")
    print("7: SALIR")
    opcion = input()

    if opcion == "1":
        print("elija una opcion")
        print("0: ver lista de empresas")
        print("1: calcular ganancias del mes")
        print("2: calcular ganancias generales")
        print("3: ver historial de ganancias por mes")
        print("4: calcular caja de ahorros")
        print("5: calcular dividendo por accion")
        print("6: calcular dividendo por accionistas")
        print("7: calcular porcentaje por accionista")
        opcion1 = input()
        if opcion1 == "0":
            for item in empresa:
                print("Nombre: ",item.Nombre," Rublo: ", item.Rublo," Abreviatura: ", item.Abreviatura)
            print("presione cualquier tecla para continuar")
            a = input()
    elif opcion == "2":
        print("elija una opcion")
        print("0: ver lista de empresas -+-")
        print("1: agregar una empresa -+-")
        print("2: agregar empleados -+-")
        print("3: agregar accionista -")
        print("4: ver lista de empleados -+")
        print("5: ver lista de accionistas -+")
        print("6: modificar sueldo empleado -")
        print("7: modificar superior empleado -")
        print("8: eliminar empleado -")
        print("9: modificar cantidad de acciones de accionista -")
        print("10: eliminar accionista -")
    elif opcion == "3":
        print("elija una opcion")
        print("0: ver lista de empresas -+-")
        print("1: agregar una compra -")
        print("2: historial de compras -+")
    elif opcion == "4":
        print("elija una opcion")
        print("0: ver lista de empresas -+-")
        print("1: ver lista de fabricantes -+")
        print("2: ver lista de materiales ")
        print("3: ingresar un fabricante")
        print("4: borrar un fabricante")
        print("5: agregar un materia")
        print("6: cambiar precio de material")
        print("7: eliminar un material")
        opcion4 = input()
        if opcion4 == "0":
            a = 1
        elif opcion4 == "1":
            a = 1
        elif opcion4 == "2":
            i = 0
            elegirFabricante = input("ingrese abreviatura del fabricante: ")
            for item in fabbricantes:
                if item.Abreviatura == elegirFabricante:
                    break
                i = i + 1
            print("lista de materiales del fabricante")
            for item2 in fabbricantes[i].materiale:
                print("nombre: ", item2.Nombre, " precio: ", item2.Precio, " unidad de medicion: ",
                      item2.UnidadMedicion)
            i = input("presione enter para continuar")
        elif opcion4 == "3":
            nuevoFabricante = fabricantes()
            nuevoFabricante.Nombre = input("ingrese el nombre: ")
            nuevoFabricante.Rublo = input("ingrese el rublo: ")
            nuevoFabricante.Abreviatura = input("ingrese la abreviatura: ")
            fabbricantes.append(nuevoFabricante)
        elif opcion4 == "4":
            elegirFabricante = input("ingrese la abreviatura del fabricante: ")
            i = 0
            encuentro = True
            for o in fabbricantes:
                if o.Abreviatura == elegirFabricante:
                    del fabbricantes[i]
                    encuentro = False
                    break
                i = i + 1
            if encuentro:
                i = input("no se encontro al fabricante. Presione enter para seguir")
        elif opcion4 == "5":
            elegirFabricante = input("ingrese la abreviatura del fabricante: ")
            i = 0
            encuentro = True
            for o in fabbricantes:
                if o.Abreviatura == elegirFabricante:
                    encuentro = False
                    break
                i = i + 1
            if encuentro:
                i = input("no se encontro al fabricante. Presione enter para seguir")
            else:
                nombre = input("ingrese el nombre del nuevo material: ")
                precio = int(input("ingrese el precio del nuevo material: "))
                um = input("ingrese la unidad de medicion del nuevo material: ")
                fabbricantes[i].crearMaterial(nombre,precio,um)
        elif opcion4 == "6":
            elegirFabricante = input("ingrese la abreviatura del fabricante del material: ")
            i = 0
            for o in fabbricantes:
                if o.Abreviatura == elegirFabricante:
                    break
                i = i + 1
            print("lista de materiales del fabricante")
            for item2 in fabbricantes[i].materiale:
                print("nombre: ", item2.Nombre, " precio: ", item2.Precio, " unidad de medicion: ",item2.UnidadMedicion)
            elegirMaterial = input("ingrese el nombre del material: ")
            for item2 in fabbricantes[i].materiale:
                if item2.Nombre == elegirMaterial:
                    item2.Precio = int(input("ingrese el nuevo precio: "))
        elif opcion4 == "7":
            elegirFabricante = input("ingrese la abreviatura del fabricante del material: ")
            i = 0
            for o in fabbricantes:
                if o.Abreviatura == elegirFabricante:
                    break
                i = i + 1
            print("lista de materiales del fabricante")
            for item2 in fabbricantes[i].materiale:
                print("nombre: ", item2.Nombre, " precio: ", item2.Precio, " unidad de medicion: ",
                      item2.UnidadMedicion)
            elegirMaterial = input("ingrese el nombre del material: ")
            o = 0
            for item2 in fabbricantes[i].materiale:
                if item2.Nombre == elegirMaterial:
                    break
                o = o + 1
            del fabbricantes[i].materiale[o]

    elif opcion == "5":
        print("elija una opcion")
        print("0: ver lista de empresas")
        print("1: agregar un producto")
        print("2: modificar un producto")
        print("3: eliminar un producto")
        print("4: agregar una categoria")
        print("5: eliminar una categoria")
        opcion5 = input()
    elif opcion == "6":
        print("elija una opcion")
        print("0: ver lista de empresas")
        print("1: agregar un pedido")
        print("2: eliminar un pedido")
        print("3: ver lista de pedidos")
        opcion6 = input()
    elif opcion == "7":
        seguir = False
