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
abrUniversal = ""
app = Flask(__name__)
@app.route('/')
@app.route('/principal', methods=['GET', 'POST'])
def principal():
    return render_template('principal.html')
@app.route('/')
@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
        for item in cliente:
            if(request.form['nicknameUsuario'] == item.nickname and request.form['password'] == item.contrasena):
                abrUniversal = item.empresaAsociada
    return render_template('ingreso.html')
@app.route('/')
@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        nuevoUsuario = usuarios()
        nuevoUsuario.nickname = request.form['nicknameUsuario']
        nuevoUsuario.contrasena = request.form['password']
        nuevoUsuario.empresaAsociada = request.form['abreviatura']
        cliente.append(nuevoUsuario)
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
        nuevaEmpresa = empresas()
        nuevaEmpresa.Nombre = request.form['empresaNombre']
        nuevaEmpresa.Rublo = request.form['empresaRublo']
        nuevaEmpresa.Abreviatura = request.form['empresaAbreviatura']
        empresa.append(nuevaEmpresa)
    return render_template('AgregarEmpresa.html',
                           title='Sign In')
@app.route('/')
@app.route('/listarEmpresas', methods=['GET','POST'])
def listarEmpresas():
    return render_template("listarEmpresas.html",
                           title='Home',
                           posts=empresa)
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
        print("0: ver lista de empresas")
        print("1: agregar una empresa")
        print("2: agregar empleados")
        print("3: agregar accionista")
        print("4: ver lista de empleados")
        print("5: ver lista de accionistas")
        print("6: modificar sueldo empleado")
        print("7: modificar superior empleado")
        print("8: eliminar empleado")
        print("9: modificar cantidad de acciones de accionista")
        print("10: eliminar accionista")
        opcion2 = input()
        if opcion2 == "0":
            for item in empresa:
                print("Nombre: ",item.Nombre," Rublo: ", item.Rublo," Abreviatura: ", item.Abreviatura)
            print("presione enter para continuar")
            a = input()
        elif opcion2 == "1":
            a = a +1
        elif opcion2 == "2":
            empresaAbreviatura = input("ingrese la abreviatura de la empresa: ")
            i = 0
            a = False
            for o in empresa:
                if o.Abreviatura == empresaAbreviatura:
                    a = True
                    break
                i = i + 1
            if a == True:
                nuevoEmpleado = empleados()
                nuevoEmpleado.nombre = input("ingrese el nombre del empleado: ")
                nuevoEmpleado.fechaIngreso = datetime.now()
                nuevoEmpleado.Profesion = input("ingrese la profesion del empleado: ")
                nuevoEmpleado.superior = input("ingrese el nombre de su superior, de lo contrario dejar vacio: ")
                nuevoEmpleado.sueldo = input("ingrese el sueldo del empleado: ")
                empresa[i].agregarEmpleado(nuevoEmpleado)
            else:
                print("no se encontro ninguna empresa")
            a = input("presione enter para continuar")
        elif opcion2 == "3":
            empresaAbreviatura = input("ingrese la abreviatura de la empresa: ")
            i = 0
            a = False
            for o in empresa:
                if o.Abreviatura == empresaAbreviatura:
                    a = True
                    break
                i = i + 1
            if a == True:
                nuevoAccionista = accionistas()
                nuevoAccionista.nombre = input("ingrese el nombre del accionista: ")
                nuevoAccionista.fechaIngreso = datetime.now()
                nuevoAccionista.cantidadAcciones = input("ingrese la cantidad de acciones: ")
                empresa[i].agregarAccionista(nuevoAccionista)
            else:
                print("no se encontro ninguna empresa")
            a = input("presione enter para continuar")
        elif opcion2 == "4":
            empresaAbreviatura = input("ingrese la abreviatura de la empresa: ")
            i = 0
            for o in empresa:
                if o.Abreviatura == empresaAbreviatura:
                    break
                i = i + 1
            for item in empresa[i].Empleados:
                print("Nombre: ", item.nombre," profesion: ", item.Profesion," sueldo: ", item.sueldo," fecha de ingreso: ", item.fechaIngreso," superior: ", item.superior)
            a = input("presione enter para continuar")
        elif opcion2 == "5":
            empresaAbreviatura = input("ingrese la abreviatura de la empresa: ")
            i = 0
            for o in empresa:
                if o.Abreviatura == empresaAbreviatura:
                    break
                i = i + 1
            for item in empresa[i].accionistas:
                print("Nombre: ", item.nombre, " fecha de ingreso: ", item.fechaIngreso, " cantidad de acciones: ", item.cantidadAcciones)
            a = input("presione enter para continuar")
        elif opcion2 == "6":
            empresaAbreviatura = input("ingrese la abreviatura de la empresa: ")
            i = 0
            for o in empresa:
                if o.Abreviatura == empresaAbreviatura:
                    break
                i = i + 1
            empleadoNombre = input("ingrese el nombre del empleado: ")
            for o in empresa[i].Empleados:
                if o.nombre == empleadoNombre:
                    o.sueldo = input("ingrese el nuevo sueldo del empleado: ")
                    break
        elif opcion2 == "7":
            empresaAbreviatura = input("ingrese la abreviatura de la empresa: ")
            i = 0
            for o in empresa:
                if o.Abreviatura == empresaAbreviatura:
                    break
                i = i + 1
            empleadoNombre = input("ingrese el nombre del empleado: ")
            for o in empresa[i].Empleados:
                if o.nombre == empleadoNombre:
                    o.superior = input("ingrese el nuevo superior del empleado: ")
                    break
        elif opcion2 == "8":
            empresaAbreviatura = input("ingrese la abreviatura de la empresa: ")
            i = 0
            for o in empresa:
                if o.Abreviatura == empresaAbreviatura:
                    break
                i = i + 1
            empleadoNombre = input("ingrese el nombre del empleado: ")
            empresa[i].eliminarEmpleado(empleadoNombre)
        elif opcion2 == "9":
            empresaAbreviatura = input("ingrese la abreviatura de la empresa: ")
            i = 0
            for o in empresa:
                if o.Abreviatura == empresaAbreviatura:
                    break
                i = i + 1
            accionistaNombre = input("ingrese el nombre del accionista: ")
            nuevaCantidad = input("ingrese la nueva cantidad de acciones: ")
            empresa[i].modificarAcciones(accionistaNombre,nuevaCantidad)
        elif opcion2 == "10":
            empresaAbreviatura = input("ingrese la abreviatura de la empresa: ")
            i = 0
            for o in empresa:
                if o.Abreviatura == empresaAbreviatura:
                    break
                i = i + 1
            accionistaNombre = input("ingrese el nombre del accionista: ")
            empresa[i].eliminarAccionista(accionistaNombre)
    elif opcion == "3":
        print("elija una opcion")
        print("0: ver lista de empresas")
        print("1: agregar una compra")
        print("2: historial de compras")
        opcion3 = input()
        if opcion3 == "0":
            for item in empresa:
                print("Nombre: ",item.Nombre," Rublo: ", item.Rublo," Abreviatura: ", item.Abreviatura)
            print("presione enter para continuar")
            a = input()
        elif opcion3 == "1":
            empresaAbreviatura = input("ingrese la abreviatura de la empresa: ")
            i = 0
            for o in empresa:
                if o.Abreviatura == empresaAbreviatura:
                    break
                i = i + 1
            nuevaCompra = compras()
            nuevaCompra.idCompra = empresa[i].obtenerIdCompra()
            nuevaCompra.Fecha = datetime.now()
            elegirFabricante = input("ingrese la abreviatura del fabricante del material a comprar: ")
            i = 0
            for o in fabbricantes:
                if o.Abreviatura == elegirFabricante:
                    break
                i = i + 1
            print("lista de materiales del fabricante")
            for item2 in fabbricantes[i].materiale:
                print("nombre: ",item2.Nombre, " precio: ", item2.Precio, " unidad de medicion: ", item2.UnidadMedicion)
            elegirMaterial = input("ingrese el nombre del material: ")
            for item2 in fabbricantes[i].materiale:
                if item2.Nombre == elegirMaterial:
                    nuevaCompra.material = item2
                    nuevaCompra.cantidad = int(input("ingrese la cantidad de la compra: "))
                    nuevaCompra.Precio = (nuevaCompra.cantidad * nuevaCompra.material.Precio)
                    empresa[i].agregarCompra(nuevaCompra)
        elif opcion3 == "2":
            empresaAbreviatura = input("ingrese la abreviatura de la empresa: ")
            i = 0
            for o in empresa:
                if o.Abreviatura == empresaAbreviatura:
                    break
                i = i + 1
            for item in empresa[i].Compras:
                print("ID: ", item.idCompra, " Fecha: ", item.Fecha," Precio: ",item.Precio, " Material: ", item.material.Nombre, " Cantidad: ", item.cantidad)
    elif opcion == "4":
        print("elija una opcion")
        print("0: ver lista de empresas")
        print("1: ver lista de fabricantes")
        print("2: ver lista de materiales")
        print("3: ingresar un fabricante")
        print("4: borrar un fabricante")
        print("5: agregar un materia")
        print("6: cambiar precio de material")
        print("7: eliminar un material")
        opcion4 = input()
        if opcion4 == "0":
            for item in empresa:
                print("Nombre: ", item.Nombre, " Rublo: ", item.Rublo, " Abreviatura: ", item.Abreviatura)
            print("presione enter para continuar")
            a = input()
        elif opcion4 == "1":
            for item in fabbricantes:
                print("Nombre: ",item.Nombre," Rublo: ", item.Rublo," Abreviatura: ", item.Abreviatura)
            print("presione enter para continuar")
            a = input()
        elif opcion4 == "2":
            i = 0
            elegirFabricante = input("ingrese abreviatura del fabricante: ")
            for item in fabbricantes:
                if item.Abreviatura == elegirFabricante:
                    break
                i = i + 1
            print("lista de materiales del fabricante")
            for item2 in fabbricantes[i].materiale:
                print("nombre: ", item2.Nombre, " precio: ", item2.Precio, " unidad de medicion: ",item2.UnidadMedicion)
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



