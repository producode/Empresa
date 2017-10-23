from datetime import datetime
from datetime import date
from Empresas.clases.empresa import empresas
from Empresas.clases.fabricante import fabricantes
from Empresas.clases.categoria import categorias
from Empresas.clases.empleado import empleados
from Empresas.clases.accionista import accionistas
from Empresas.clases.compra import compras
from Empresas.clases.usuario import usuarios
from Empresas.clases.producto import productos
from flask import Flask
from flask import render_template
from flask import request
from pymongo import MongoClient

empresa = []
fabbricantes = []
categoriaLista = []
cliente = []
abrUniversal = "eds"
fabUniversal = "aaa"
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection


def ingresarEmpresa2(nombre,rublo,abreviatura):
    nuevaEmpresa = empresas()
    result = db.empresa.insert_one({"nombre": nombre,"rublo": rublo,"abreviatura": abreviatura})
    result.inserted_id
    cursor = db.empresa.find()
    nuevaEmpresa.Nombre = nombre
    nuevaEmpresa.Rublo = rublo
    nuevaEmpresa.Abreviatura = abreviatura
    empresa.append(nuevaEmpresa)
    for item in cursor:
        print(item)
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
def ingresarEmpleado2(cuit,nombre,profesion,superior,sueldo):
    nuevoEmpleado = empleados()
    result = db.empleado.insert_one({"cuit": cuit,"nombre": nombre,"fecha de ingreso": datetime.now(),"profesion": profesion, "superior": superior, "sueldo": sueldo})
    result.inserted_id
    cursor = db.empleado.find()
    nuevoEmpleado.cuit = cuit
    nuevoEmpleado.nombre = nombre
    nuevoEmpleado.fechaIngreso = datetime.now()
    nuevoEmpleado.Profesion = profesion
    nuevoEmpleado.superior = superior
    nuevoEmpleado.sueldo = sueldo
    for item in cursor:
        print(item)
    empresa[listarEmpleados2()].agregarEmpleado(nuevoEmpleado)
def ingresarAccionista2(cuit,nombre,cantidad):
    result = db.accionista.insert_one({"cuit": cuit,"nombre": nombre,"fecha de ingreso": datetime.now(),"cantidad de acciones": cantidad})
    result.inserted_id
    cursor = db.accionista.find()
    nuevoAccionista = accionistas()
    nuevoAccionista.cuit = cuit
    nuevoAccionista.nombre = nombre
    nuevoAccionista.fechaIngreso = datetime.now()
    nuevoAccionista.cantidadAcciones = cantidad
    for item in cursor:
        print(item)
    empresa[listarEmpleados2()].agregarAccionista(nuevoAccionista)
def ingresarCompra2(fabricante,material,cantidad):
    nuevaCompra = compras()
    nuevaCompra.idCompra = empresa[listarEmpleados2()].obtenerIdCompra()
    nuevaCompra.Fecha = datetime.now()
    for item2 in fabbricantes[elegirFabricane(fabricante)].materiale:
        if item2.Nombre == material:
            result = db.compra.insert_one({"idCompra": empresa[listarEmpleados2()].obtenerIdCompra() ,"fecha de compra": datetime.now(),"material": item2.Nombre, "cantidad": int(cantidad), "precio": (nuevaCompra.cantidad * nuevaCompra.material.Precio)})
            result.inserted_id
            cursor = db.compra.find()
            nuevaCompra.material = item2
            nuevaCompra.cantidad = int(cantidad)
            nuevaCompra.Precio = (nuevaCompra.cantidad * nuevaCompra.material.Precio)
            empresa[listarEmpleados2()].agregarCompra(nuevaCompra)
    for item in cursor:
        print(item)
    cursor = db.empresa.delete_many({"nombre": nombre})
def ingresarFabricante2(nombre,rublo,abreviatura):
    result = db.fabricante.insert_one({"nombre": nombre, "rublo": rublo, "abreviatura": abreviatura})
    result.inserted_id
    cursor = db.fabricante.find()
    nuevoFabricante = fabricantes()
    nuevoFabricante.Nombre = nombre
    nuevoFabricante.Rublo = rublo
    nuevoFabricante.Abreviatura = abreviatura
    for item in cursor:
        print(item)
    fabbricantes.append(nuevoFabricante)
def ingresarMaterial2(abreviatura,nombre,precio,um):
    fabbricantes[elegirFabricane(abreviatura)].crearMaterial(nombre, precio, um)
    result = db.material.insert_one({"nombre": nombre, "precio": precio, "unidad de medicion": um})
    result.inserted_id
    cursor = db.material.find()
    for item in cursor:
        print(item)
def ingresarProducto2(nombre,Coste,Descripcion,categoria,material):
    nuevoproducto = productos()
    result = db.producto.insert_one({"idProducto": empresa[listarEmpleados2()].obtenerIdPedido(),"nombre": nombre, "coste": Coste, "descripcion": Descripcion,"categoria": categoria,"material": material})
    result.inserted_id
    cursor = db.producto.find()
    for item in cursor:
        print(item)
    nuevoproducto.Nombre = nombre
    nuevoproducto.Coste = Coste
    nuevoproducto.Descripcion = Descripcion
    nuevoproducto.Categoria = categoria
    nuevoproducto.material = material
    nuevoproducto.idProducto = empresa[listarEmpleados2()].obtenerIdPedido()
    empresa[listarEmpleados2()].Productos.append(nuevoproducto)
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
def listarMateriales2(abreviatura):
    fabUniversal = abreviatura
def modificarEmpleado2(cuit,superior,sueldo):
    for o in empresa[listarEmpleados2()].Empleados:
        if o.cuit == cuit:
            o.superior = superior
            o.sueldo = sueldo
            break
def modificarAccionista2(cuit,cantidad):
    empresa[listarEmpleados2()].modificarAcciones(cuit, cantidad)
def modificarMaterial2(abreviatura,nombre,precio):
    for item in fabbricantes[elegirFabricane(abreviatura)].materiale:
        if item.Nombre == nombre:
            item.Precio = precio
def eliminarEmpleado2(cuit):
    empresa[listarEmpleados2()].eliminarEmpleado(cuit)
def eliminarAccionista2(cuit):
    empresa[listarEmpleados2()].eliminarAccionista(cuit)
def eliminarFabricante2(nombre):
    del fabbricantes[elegirFabricane(nombre)]
def eliminarMaterial2(abreviatura,nombre):
    o = 0
    for item2 in fabbricantes[elegirFabricane(abreviatura)].materiale:
        if item2.Nombre == nombre:
            break
        o = o + 1
    del fabbricantes[elegirFabricane(abreviatura)].materiale[o]
def elegirFabricane(fabricante):
    i = 0
    for o in fabbricantes:
        if o.Abreviatura == fabricante:
            break
        i = i + 1
    return i
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
    print("ahora")
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
@app.route('/ingresarFabricante', methods=['GET', 'POST'])
def ingresarFabricante():
    if request.method == 'POST':
        ingresarFabricante2(request.form['Nombre'],request.form['Rublo'],request.form['Abreviatura'])
    return render_template('ingresarFabricante.html',
                           title='Sign In')
@app.route('/')
@app.route('/ingresarAccionista', methods=['GET','POST'])
def ingresarAccionistas():
    if request.method == 'POST':
        ingresarAccionista2(request.form['cuit'],request.form['nombre'],request.form['cantidadAcciones'])
    return render_template("ingresarAccionista.html")
@app.route('/')
@app.route('/ingresarEmpleado', methods=['GET','POST'])
def ingresarEmpleado():
    if request.method == 'POST':
        ingresarEmpleado2(request.form['cuit'],request.form['nombre'],request.form['profesion'], request.form['superior'],request.form['sueldo'])
    return render_template("ingresarEmpleado.html")
@app.route('/')
@app.route('/ingresarMaterial', methods=['GET','POST'])
def ingresarMaterial():
    if request.method == 'POST':
        ingresarMaterial2(request.form['abreviatura'],request.form['nombre'],request.form['precio'],request.form['um'])
    return render_template("ingresarMaterial.html")
@app.route('/')
@app.route('/ingresarCompra', methods=['GET','POST'])
def ingresarCompra():
    if request.method == 'POST':
        ingresarCompra2(request.form['abreviatura'],request.form['nombre'],request.form['cantidad'])
    return render_template("ingresarCompra.html")
@app.route('/')
@app.route('/ingresarProducto', methods=['GET','POST'])
def ingresarProducto():
    if request.method == 'POST':
        ingresarProducto(request.form['nombre'],request.form['coste'],request.form['descripcion'],request.form['categoria'])
    return render_template("ingresarProducto.html")
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
    print(listarEmpleados2())
    uno = empresa[listarEmpleados2()].Empleados
    return render_template("listarEmpleados.html",
                           title='Home',
                           posts=uno)
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
@app.route('/listarMaterialesp', methods=['GET','POST'])
def listarMaterialesp():
    if request.method():
        listarMateriales2(request.form['abreviatura'])
    return render_template("listarMaterialesp.html")
@app.route('/')
@app.route('/listarMaterialess', methods=['GET','POST'])
def listarMaterialess():
    return render_template("listarMaterialess",
                           title='Home',
                           posts=fabbricantes[elegirFabricane(fabUniversal)].materiale)
@app.route('/')
@app.route('/modificarEmpleado', methods=['GET','POST'])
def modificarEmpleado():
    if request.method == 'POST':
        modificarEmpleado2(request.form['cuit'],request.form['superior'],request.form['sueldo'])
    return render_template("modificarEmpleado.html")
@app.route('/')
@app.route('/modificarMaterial', methods=['GET','POST'])
def modificarMaterial():
    if request.method == 'POST':
        modificarMaterial2(request.form['abreviatura'],request.form['nombre'],request.form['precio'])
    return render_template("modificarMaterial.html")
@app.route('/')
@app.route('/modificarAccionista', methods=['GET','POST'])
def modificarAccionista():
    if request.method == 'POST':
        modificarAccionista2(request.form['cuit'],request.form['cantidad'])
    return render_template("modificarAccionista.html")
@app.route('/')
@app.route('/eliminarFabricante', methods=['GET','POST'])
def eliminarFabricante():
    if request.method == 'POST':
        eliminarFabricante2(request.form['abreviatura'])
    return render_template("eliminarFabricante.html")
@app.route('/')
@app.route('/eliminarMaterial', methods=['GET','POST'])
def eliminarMaterial():
    if request.method == 'POST':
        eliminarMaterial2(request.form['abreviatura'],request.form['nombre'])
    return render_template("eliminarMaterial.html")
@app.route('/')
@app.route('/eliminarEmpleado', methods=['GET','POST'])
def eliminarEmpleado():
    if request.method == 'POST':
        eliminarEmpleado2(request.form['cuit'])
    return render_template("eliminarEmpleado.html")
@app.route('/')
@app.route('/eliminarAccionista', methods=['GET','POST'])
def eliminarAccionista():
    if request.method == 'POST':
        eliminarAccionista2(request.form['cuit'])
    return render_template("eliminarAccionista.html")
@app.route('/')
@app.route('/verFabricante', methods=['GET','POST'])
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
    print("2: EMPRESAS -+-")
    print("3: COMPRAS -+-")
    print("4: MATERIALES-+-")
    print("5: PRODUCTOS")
    print("6: PEDIDOS")
    print("7: SALIR-+-")
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
        print("3: agregar accionista -+-")
        print("4: ver lista de empleados -+-")
        print("5: ver lista de accionistas -+-")
        print("6: modificar sueldo empleado -+-")
        print("7: modificar superior empleado -+-")
        print("8: eliminar empleado -+-")
        print("9: modificar cantidad de acciones de accionista -+-")
        print("10: eliminar accionista -+-")
    elif opcion == "3":
        print("elija una opcion")
        print("0: ver lista de empresas -+-")
        print("1: agregar una compra -+-")
        print("2: historial de compras -+-")
    elif opcion == "4":
        print("elija una opcion")
        print("0: ver lista de empresas -+-")
        print("1: ver lista de fabricantes -+-")
        print("2: ver lista de materiales -+-")
        print("3: ingresar un fabricante -+-")
        print("4: borrar un fabricante -+-")
        print("5: agregar un materia -+-")
        print("6: cambiar precio de material -+-")
        print("7: eliminar un material -+-")
    elif opcion == "5":
        print("1: agregar un producto -+")
        print("2: modificar un producto ")
        print("3: eliminar un producto")
        print("4: agregar una categoria")
        print("5: eliminar una categoria")
        print("0: ver lista de empresas")
        print("1: agregar un pedido")
        print("2: eliminar un pedido")
        print("3: ver lista de pedidos")

        opcion5 = input()
    elif opcion == "6":
        print("elija una opcion")
        print("0: ver lista de empresas")

        opcion6 = input()
    elif opcion == "7":
        seguir = False
