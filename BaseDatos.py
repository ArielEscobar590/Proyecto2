Motores_Dic = {}
Ventas_Dic = {}
Compras_Dic = {}

class Empleados:
    def __init__(self):
        self.empleados = {}
        self.cargar_empleados()

    def cargar_empleados(self):
        try:
            with open("empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo, puesto = linea.split(":")
                        self.empleados[nit] = {
                            "Nombre": nombre,
                            "Direccion": direccion,
                            "Telefono": telefono,
                            "Correo": correo,
                            "Puesto" :puesto
                        }
            print("Empleados importados desde empleados.txt")
        except FileNotFoundError:
            print("No existe el archivo empleados.txt, se creará uno nuevo al guardar.")

    def guardar_empleados(self):
        with open("empleados.txt", "w", encoding="utf-8") as archivo:
            for nit, datos in self.empleados.items():
                archivo.write(f"{nit}:{datos['Nombre']}:{datos['Direccion']}:{datos['Telefono']}:{datos['Correo']}:{datos['Puesto']}\n")

    def agregar_empleado(self, nit, nombre, direccion, telefono, correo, puesto):
        self.empleados[nit] = {
            "Nombre": nombre,
            "Direccion": direccion,
            "Telefono": telefono,
            "Correo": correo,
            "Puesto": puesto
        }
        self.guardar_empleados()
        print(f"Empleado con NIT {nit} agregado y guardado correctamente.")

    def mostrar_empleados(self):
        if self.empleados:
            print("\nLista de empleados:")
            for nit, datos in self.empleados.items():
                print(f"\nNIT: {nit}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
        else:
            print("No hay empleados registrados.")


class Clientes:
    def __init__(self):
        self.clientes = {}
        self.cargar_clientes()

    def cargar_clientes(self):
        try:
            with open("clientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo = linea.split(":")
                        self.clientes[nit] = {
                            "Nombre": nombre,
                            "Direccion": direccion,
                            "Telefono": telefono,
                            "Correo": correo
                        }
            print("Clientes importados desde clientes.txt")
        except FileNotFoundError:
            print("No existe el archivo clientes.txt, se creará uno nuevo al guardar.")

    def guardar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for nit, datos in self.clientes.items():
                archivo.write(f"{nit}:{datos['Nombre']}:{datos['Direccion']}:{datos['Telefono']}:{datos['Correo']}\n")

    def agregar_cliente(self, nit, nombre, direccion, telefono, correo):
        self.clientes[nit] = {
            "Nombre": nombre,
            "Direccion": direccion,
            "Telefono": telefono,
            "Correo": correo
        }
        self.guardar_clientes()
        print(f"Cliente con NIT {nit} agregado y guardado correctamente.")

    def mostrar_clientes(self):
        if self.clientes:
            print("\nLista de clientes:")
            for nit, datos in self.clientes.items():
                print(f"\nNIT: {nit}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
        else:
            print("No hay clientes registrados.")

class Proveedores:
    def __init__(self):
        self.proveedores = {}
        self.cargar_proveedores()

    def cargar_proveedores(self):
        try:
            with open("proveedores.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo, empresa = linea.split(":")
                        self.proveedores[nit] = {
                            "Nombre": nombre,
                            "Direccion": direccion,
                            "Telefono": telefono,
                            "Correo": correo,
                            "Empresa": empresa
                        }
            print("Proveedores importados desde proveedores.txt")
        except FileNotFoundError:
            print("No existe el archivo proveedores.txt, se creará uno nuevo al guardar.")

    def guardar_proveedores(self):
        with open("proveedores.txt", "w", encoding="utf-8") as archivo:
            for nit, datos in self.proveedores.items():
                archivo.write(f"{nit}:{datos['Nombre']}:{datos['Direccion']}:{datos['Telefono']}:{datos['Correo']}:{datos['Empresa']}\n")

    def agregar_cliente(self, nit, nombre, direccion, telefono, correo, empresa):
        self.proveedores[nit] = {
            "Nombre": nombre,
            "Direccion": direccion,
            "Telefono": telefono,
            "Correo": correo,
            "Empresa": empresa
        }
        self.guardar_proveedores()
        print(f"Proveedor con NIT {nit} agregado y guardado correctamente.")

    def mostrar_proveedores(self):
        if self.proveedores:
            print("\nLista de clientes:")
            for nit, datos in self.proveedores.items():
                print(f"\nNIT: {nit}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
        else:
            print("No hay proveedores registrados.")

class Motores:
    def __init__(self):
        self.motores = {}
        self.cargar_motores()

    def cargar_motores(self):
        try:
            with open("motores.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_codigo, cilindrada, categoria, precio, stock, total_compras, total_ventas = linea.split(":")
                        self.motores[id_codigo] = {
                            "Cilindrada": cilindrada,
                            "Categoria": categoria,
                            "Precio": precio,
                            "Stock": stock,
                            "Total_Compras": total_compras,
                            "Total_Ventas": total_ventas
                        }
            print("Motores importados desde motores.txt")
        except FileNotFoundError:
            print("No existe el archivo motores.txt, se creará uno nuevo al guardar.")

    def guardar_motores(self):
        with open("motores.txt", "w", encoding="utf-8") as archivo:
            for id_codigo, datos in self.motores.items():
                archivo.write(f"{id_codigo}:{datos['Cilindrada']}:{datos['Categoria']}:{datos['Precio']}:{datos['Stock']}:{datos['Total_Compras']}:{datos['Total_Ventas']}\n")

    def agregar_cliente(self, id_codigo, cilindrada, categoria, precio, stock, total_compras, total_ventas):
        self.motores[id_codigo] = {
            "Cilindrada": cilindrada,
            "Categoria": categoria,
            "Precio": precio,
            "Stock": stock,
            "Total_Compras": total_compras,
            "Total_Ventas": total_ventas
        }
        self.guardar_motores()
        print(f"Motor con id_codigo {id_codigo} agregado y guardado correctamente.")

    def mostrar_motores(self):
        if self.motores:
            print("\nLista de motores:")
            for id_codigo, datos in self.motores.items():
                print(f"\nId: {id_codigo}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
        else:
            print("No hay motores registrados.")

class Categorias:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Compras:
    def __init__(self, id_compra, proveedor, fecha):
        self.id_compra = id_compra
        self.proveedor = proveedor
        self.fecha = fecha
        self.detalles = []

    def agregar_detalle(self, motor, cantidad):
        detalle = DetalleCompras(motor, cantidad)
        self.detalles.append(detalle)
        motor.stock += cantidad
        motor.total_compras += cantidad

class DetalleCompras:
    def __init__(self, motor, cantidad):
        self.motor = motor
        self.cantidad = cantidad

class Ventas:
    def __init__(self, id_venta, cliente, fecha):
        self.id_venta = id_venta
        self.cliente = cliente
        self.fecha = fecha
        self.detalles = []

    def agregar_detalle(self, motor, cantidad):
        if motor.stock >= cantidad:
            detalle = DetalleVentas(motor, cantidad)
            self.detalles.append(detalle)
            motor.stock -= cantidad
            motor.total_ventas += cantidad
        else:
            print(f"No hay stock suficiente de {motor.nombre}")

class DetalleVentas:
    def __init__(self, motor, cantidad):
        self.motor = motor
        self.cantidad = cantidad

class Inventario:
    def Agregar(self):
        try:
            agre = int(input("Cuantos productos desea ingresar: "))
            for a in range(agre):
                cod = input("Ingrese código del producto: ")
                if cod in Motores_Dic:
                    print("Ya existe un producto con ese código.")
                    return

                nom = input("Ingrese nombre del producto: ")
                cat = input("Ingrese categoría: ")
                pre = float(input("Ingrese precio del producto (Q): "))
                if pre <= 0:
                    print("Precio inválido ")
                    return
                sto = int(input("Ingrese cantidad del producto: "))

                p = Motores(cod, nom, cat, pre, sto)
                Motores_Dic[cod] = p
                print("Producto agregado con éxito.\n")
        except ValueError:
            print("Error: Ingresaste un dato inválido.\n")

    def eliminar(self):
        eli = input("Ingrese código del motor a eliminar: ")
        if eli not in Motores_Dic:
            print("No existe en Inventario\n")
        else:
            eliminado = Motores_Dic.pop(eli)
            print(f"Motor Eliminado: {eliminado.nombre}")
            print("Eliminado con éxito\n")

class Busqueda:
    def Buscador(self, lista, criterio, valor):
        resultados = []
        valor = valor.lower().strip()

        for motor in lista:
            if criterio == 1:  # Código
                if motor.id_codigo.lower() == valor:
                    resultados.append(motor)
            elif criterio == 2:  # Nombre
                if valor in motor.nombre.lower():
                    resultados.append(motor)
            elif criterio == 3:  # Categoría
                if valor in motor.categoria.lower():
                    resultados.append(motor)
        return resultados

class Listar:
    def quicksort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return self.quicksort(menores) + iguales + self.quicksort(mayores)

class Modificar:
    def actualizar(self):
        codigo = input("Ingrese el código del Motor a actualizar: ")
        if codigo not in Motores_Dic:
            print("No existe un Motor con ese código.")
            return

        producto = Motores_Dic[codigo]
        print("\nMotor actual:")
        producto.Mostrar()

        try:
            nuevo_precio = input("Ingrese nuevo precio (deje vacío para no cambiar): ")
            nuevo_stock = input("Ingrese nuevo stock (deje vacío para no cambiar): ")

            if nuevo_precio.strip() != "":
                nuevo_precio = float(nuevo_precio)
                if nuevo_precio > 0:
                    producto.precio = nuevo_precio
                else:
                    print("Precio inválido, no se actualizó.")

            if nuevo_stock.strip() != "":
                nuevo_stock = int(nuevo_stock)
                if nuevo_stock >= 0:
                    producto.stock = nuevo_stock
                else:
                    print("Stock inválido, no se actualizó.")

            print("\nMotor actualizado con éxito:")
            producto.Mostrar()
        except ValueError:
            print("Error: dato inválido, no se realizaron cambios.\n")

class Menus:
    def MenuPrincipal(self):
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ingreso de producto")
        print("2. Listar Inventario")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Modificar producto")
        print("6. Registrar venta")
        print("7. Registrar compra")
        print("8. Salir")

    def Submenu1(self):
        print("\n--- ORDENAR INVENTARIO ---")
        print("1. Por nombre")
        print("2. Por precio")
        print("3. Por stock")

    def Submenu2(self):
        print("\n--- BUSCAR MOTOR ---")
        print("1. Por código")
        print("2. Por nombre")
        print("3. Por categoría")

class Main:
    def Main(self):
        clientes = Clientes()
        inven = Inventario()
        listar = Listar()
        bus = Busqueda()
        menus = Menus()
        modi = Modificar()
        op = 0
        while op != 8:
            try:
                menus.MenuPrincipal()
                op = int(input("Ingrese opción a ejecutar: "))
                match op:
                    case 1:
                        inven.Agregar()
                    case 2:
                        if not Motores_Dic:
                            print("\nInventario vacío.")
                        else:
                            menus.Submenu1()
                            ordenar = int(input("Ingrese una opción: "))
                            if ordenar == 1:
                                listaordenada = listar.quicksort([p.nombre for p in Motores_Dic.values()])
                            elif ordenar == 2:
                                listaordenada = listar.quicksort([p.precio for p in Motores_Dic.values()])
                            elif ordenar == 3:
                                listaordenada = listar.quicksort([p.stock for p in Motores_Dic.values()])
                            else:
                                print("Opción inválida.")
                                listaordenada = []

                            print("\nInventario ordenado:\n")
                            for valor in listaordenada:
                                for producto in Motores_Dic.values():
                                    if (ordenar == 1 and producto.nombre == valor or
                                        ordenar == 2 and producto.precio == valor or
                                        ordenar == 3 and producto.stock == valor):
                                        producto.Mostrar()
                    case 3:
                        if not Motores_Dic:
                            print("\nInventario vacío.")
                        else:
                            menus.Submenu2()
                            buscar = int(input("Ingrese una opción: "))
                            valor_a_buscar = input("Ingrese valor a buscar: ")
                            resultados = bus.Buscador(list(Motores_Dic.values()), buscar, valor_a_buscar)
                            if resultados:
                                print("\nResultados de la búsqueda:\n")
                                for producto in resultados:
                                    producto.Mostrar()
                            else:
                                print("No se encontraron Motores con ese criterio.")
                    case 4:
                        inven.eliminar()
                    case 5:
                        modi.actualizar()
                    case 6:
                        print("\n--- Registrar venta ---")
                        id_venta = input("ID de la venta: ")
                        cliente = input("Cliente: ")
                        fecha = input("Fecha: ")
                        venta = Ventas(id_venta, cliente, fecha)
                        cod = input("Código del motor vendido: ")
                        if cod in Motores_Dic:
                            cantidad = int(input("Cantidad: "))
                            venta.agregar_detalle(Motores_Dic[cod], cantidad)
                            Ventas_Dic[id_venta] = venta
                            print("Venta registrada con éxito.")
                        else:
                            print("El motor no existe.")
                    case 7:
                        print("\n--- Registrar compra ---")
                        id_compra = input("ID de la compra: ")
                        proveedor = input("Proveedor: ")
                        fecha = input("Fecha: ")
                        compra = Compras(id_compra, proveedor, fecha)
                        cod = input("Código del motor comprado: ")
                        if cod in Motores_Dic:
                            cantidad = int(input("Cantidad: "))
                            compra.agregar_detalle(Motores_Dic[cod], cantidad)
                            Compras_Dic[id_compra] = compra
                            print("Compra registrada con éxito.")
                        else:
                            print("El motor no existe.")
                    case 8:
                        print("Fin de programa")
                    case _:
                        print("Opción no válida")
            except ValueError:
                print("Ingrese una opción válida")
            except Exception as e:
                print(f"Error: {e}")

principal = Main()
principal.Main()
