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
                            "Puesto": puesto
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


class Vendedor(Empleados):
    def __init__(self):
        super().__init__()
        self.vendedores = {nit: datos for nit, datos in self.empleados.items() if datos["Puesto"].lower() == "vendedor"}

    def existe_vendedor(self):
        return len(self.vendedores) > 0


class Bodeguero(Empleados):
    def __init__(self):
        super().__init__()
        self.bodegueros = {nit: datos for nit, datos in self.empleados.items() if datos["Puesto"].lower() == "bodeguero"}

    def existe_bodeguero(self):
        return len(self.bodegueros) > 0

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
                            "Precio": float(precio),
                            "Stock": int(stock),
                            "Total_Compras": int(total_compras),
                            "Total_Ventas": int(total_ventas)
                        }
            print("Motores importados desde motores.txt")
        except FileNotFoundError:
            print("No existe el archivo motores.txt, se creará uno nuevo al guardar.")

    def guardar_motores(self):
        with open("motores.txt", "w", encoding="utf-8") as archivo:
            for id_codigo, datos in self.motores.items():
                archivo.write(f"{id_codigo}:{datos['Cilindrada']}:{datos['Categoria']}:{datos['Precio']}:{datos['Stock']}:{datos['Total_Compras']}:{datos['Total_Ventas']}\n")

    def mostrar_motores(self):
        if self.motores:
            print("\nLista de motores:")
            for id_codigo, datos in self.motores.items():
                print(f"\nId: {id_codigo}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
        else:
            print("No hay motores registrados.")

class Inventario:
    def __init__(self):
        self.motores = Motores()

    def agregar(self):
        try:
            cod = input("Ingrese código del motor: ")
            if cod in self.motores.motores:
                print("Ya existe un motor con ese código.")
                return

            cilindrada = input("Ingrese cilindrada: ")
            cat = input("Ingrese categoría: ")
            pre = float(input("Ingrese precio del producto (Q): "))
            if pre <= 0:
                print("Precio inválido ")
                return
            sto = int(input("Ingrese cantidad del producto: "))

            self.motores.motores[cod] = {
                "Cilindrada": cilindrada,
                "Categoria": cat,
                "Precio": pre,
                "Stock": sto,
                "Total_Compras": 0,
                "Total_Ventas": 0
            }
            self.motores.guardar_motores()
            print("Producto agregado con éxito y guardado en archivo.\n")
        except ValueError:
            print("Error: Ingresaste un dato inválido.\n")

    def eliminar(self):
        eli = input("Ingrese código del motor a eliminar: ")
        if eli not in self.motores.motores:
            print("No existe en Inventario\n")
        else:
            eliminado = self.motores.motores.pop(eli)
            self.motores.guardar_motores()
            print(f"Motor Eliminado: {eliminado['Cilindrada']} - {eliminado['Categoria']}")
            print("Eliminado con éxito\n")

    def buscar(self):
        cod = input("Ingrese código a buscar: ")
        if cod in self.motores.motores:
            print("\nMotor encontrado:")
            for k, v in self.motores.motores[cod].items():
                print(f"{k}: {v}")
        else:
            print("No existe un motor con ese código.")

    def modificar(self):
        codigo = input("Ingrese el código del Motor a actualizar: ")
        if codigo not in self.motores.motores:
            print("No existe un Motor con ese código.")
            return

        producto = self.motores.motores[codigo]
        print("\nMotor actual:")
        for k, v in producto.items():
            print(f"{k}: {v}")

        try:
            nuevo_precio = input("Ingrese nuevo precio (deje vacío para no cambiar): ")
            nuevo_stock = input("Ingrese nuevo stock (deje vacío para no cambiar): ")

            if nuevo_precio.strip() != "":
                nuevo_precio = float(nuevo_precio)
                if nuevo_precio > 0:
                    producto["Precio"] = nuevo_precio
                else:
                    print("Precio inválido, no se actualizó.")

            if nuevo_stock.strip() != "":
                nuevo_stock = int(nuevo_stock)
                if nuevo_stock >= 0:
                    producto["Stock"] = nuevo_stock
                else:
                    print("Stock inválido, no se actualizó.")

            self.motores.guardar_motores()
            print("\nMotor actualizado con éxito y guardado en archivo.")
        except ValueError:
            print("Error: dato inválido, no se realizaron cambios.\n")

class Ventas:
    def __init__(self, id_venta, cliente, fecha):
        self.id_venta = id_venta
        self.cliente = cliente
        self.fecha = fecha
        self.detalles = []

    def agregar_detalle(self, motor, cantidad):
        if motor["Stock"] >= cantidad:
            motor["Stock"] -= cantidad
            motor["Total_Ventas"] += cantidad
            self.detalles.append({"Motor": motor, "Cantidad": cantidad})
        else:
            print("No hay stock suficiente.")


class Compras:
    def __init__(self, id_compra, proveedor, fecha):
        self.id_compra = id_compra
        self.proveedor = proveedor
        self.fecha = fecha
        self.detalles = []

    def agregar_detalle(self, motor, cantidad):
        motor["Stock"] += cantidad
        motor["Total_Compras"] += cantidad
        self.detalles.append({"Motor": motor, "Cantidad": cantidad})


class Menus:
    def MenuPrincipal(self):
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ingresar motor")
        print("2. Listar Inventario")
        print("3. Buscar motor")
        print("4. Eliminar motor")
        print("5. Modificar motor")
        print("6. Ingresar categorias")
        print("7. Listar categorias")
        print("8. Eliminar categorias")
        print("9. Registrar venta")
        print("10. Registrar compra")
        print("11. Salir")


class Main:
    def Main(self):
        inven = Inventario()
        menus = Menus()
        vendedores = Vendedor()
        bodegueros = Bodeguero()

        op = 0
        while op != 11:
            try:
                menus.MenuPrincipal()
                op = int(input("Ingrese opción a ejecutar: "))
                match op:
                    case 1:
                        inven.agregar()
                    case 2:
                        inven.motores.mostrar_motores()
                    case 3:
                        inven.buscar()
                    case 4:
                        inven.eliminar()
                    case 5:
                        inven.modificar()
                    case 6:
                        pass
                    case 7:
                        pass
                    case 8:
                        pass
                    case 9:

                            print("\n--- Registrar venta ---")
                            id_venta = input("ID de la venta: ")
                            cliente = input("Cliente: ")
                            fecha = input("Fecha: ")
                            venta = Ventas(id_venta, cliente, fecha)
                            cod = input("Código del motor vendido: ")
                            if cod in inven.motores.motores:
                                cantidad = int(input("Cantidad: "))
                                venta.agregar_detalle(inven.motores.motores[cod], cantidad)
                                inven.motores.guardar_motores()
                                Ventas_Dic[id_venta] = venta
                                print("Venta registrada con éxito.")
                            else:
                                print("El motor no existe.")
                    case 10:

                            print("\n--- Registrar compra ---")
                            id_compra = input("ID de la compra: ")
                            proveedor = input("Proveedor: ")
                            fecha = input("Fecha: ")
                            compra = Compras(id_compra, proveedor, fecha)
                            cod = input("Código del motor comprado: ")
                            if cod in inven.motores.motores:
                                cantidad = int(input("Cantidad: "))
                                compra.agregar_detalle(inven.motores.motores[cod], cantidad)
                                inven.motores.guardar_motores()
                                Compras_Dic[id_compra] = compra
                                print("Compra registrada con éxito.")
                            else:
                                print("El motor no existe.")
                    case 11:
                        print("Fin de programa")
                    case _:
                        print("Opción no válida")
            except ValueError:
                print("Ingrese una opción válida")
            except Exception as e:
                print(f"Error: {e}")

principal = Main()
principal.Main()
