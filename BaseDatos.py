class Personas:
    def __init__(self, nombre, direccion, telefono, correo):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

class Empleados(Personas):
    pass

class Clientes(Personas):
    pass

class Proveedores(Personas):
    pass

class Motores:
    def __init__(self, id_codigo, num_motor, precio, cilindrada, total_compras=0, total_ventas=0, stock=0):
        self.id_codigo = id_codigo
        self.num_motor = num_motor
        self.precio = precio
        self.cilindrada = cilindrada
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock

class Categorias:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Ventas:
    pass

class DetalleVentas:
    pass

class Compras:
    pass

class DetalleCompras:
    pass



class Inventario:
    def Agregar(self):
        try:
            agre = int(input("Cuantos productos desea ingresar:  "))
            for a in range(agre):

                cod = input("Ingrese código del producto: ")
                if cod in Motores_Dic:
                    print(" Ya existe un producto con ese código.")
                    return

                nom = input("Ingrese nombre del producto: ")
                cat = input("Ingrese categoría: ")
                pre = float(input("Ingrese precio del producto (Q): "))
                if pre <= 0:
                    print("Precio invalido ")
                else:
                    sto = int(input("Ingrese cantidad del producto: "))

                p = Motores(cod, nom, cat, pre, sto)
                Motores_Dic[cod] = p
                print(" Producto agregado con éxito.\n")
        except ValueError:
            print("Error: Ingresaste un dato inválido.\n")

    def actualizar(self):
        codigo = input("Ingrese el código del producto a actualizar: ")
        if codigo not in Motores_Dic:
            print("No existe un producto con ese código.")
            return

        producto = Motores_Dic[codigo]
        print("\nProducto actual:")
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

            print("\nProducto actualizado con éxito:")
            producto.Mostrar()

        except ValueError:
            print("Error: dato inválido, no se realizaron cambios.\n")

    def eliminar(self, codigo=None):
        eli = input("Ingrese codigo de producto a eliminar:  ")
        if eli not in Motores_Dic:
            print("No existe en dicionario\n")
        else:
            eli = Motores_Dic.pop(eli)
            print(f"Producto Eliminado:  {eli.nombre}  ")
            print("Eliminado con exito\n")

class Busqueda:
    def Buscardor(self, lista, criterio, valor):
        resultados = []
        valor = valor.lower().strip()

        for producto in lista:
            if criterio == 1:
                if producto.codigo == valor:
                    resultados.append(producto)
            elif criterio == 2:
                if valor in producto.nombre.lower():
                    resultados.append(producto)
            elif criterio == 3:
                if valor in producto.categoria.lower():
                    resultados.append(producto)

        return resultados

class Listar:
    pass

class Modificar:
    pass

class Menus:
    def MenuPrincipal(self):
        print("--Menu principal---")

    def Submenu1(self):
        print("--Menu principal2---")

    def Submenu2(self):
        pass

class Main:
    def Main(self):
        inven = Inventario()
        listar = Listar()
        bus = Busqueda()
        menus = Menus()
        op = 0
        while op != 6:
            try:
                menus.MenuPrincipal()
                op = int(input("Ingrese opcion a ejecutar:   "))
                match op:
                    case 1:
                        inven.Agregar()
                    case 2:
                        if not Motores_Dic:
                            print("\n Inventario vacío.")
                        else:
                            menus.Submenu1()
                            ordenar = int(input("Ingrese una opción: "))
                            lista_nombre = [p.nombre for p in Motores_Dic.values()]
                            lista_stock = [p.stock for p in Motores_Dic.values()]
                            lista_precio = [p.precio for p in Motores_Dic.values()]
                            if ordenar == 1:
                                listaordenada = listar.quicksort(lista_nombre)
                            elif ordenar == 2:
                                listaordenada = listar.quicksort(lista_precio)
                            elif ordenar == 3:
                                listaordenada = listar.quicksort(lista_stock)
                            else:
                                print("Opción inválida.")
                                listaordenada = []
                            print("\nInventario ordenado:\n")
                            for valor in listaordenada:
                                for producto in Motores_Dic.values():
                                    if (ordenar == 1 and producto.nombre == valor) or (
                                            ordenar == 2 and producto.precio == valor) or (
                                            ordenar == 3 and producto.stock == valor):
                                        producto.Mostrar()
                    case 3:
                        if not Motores_Dic:
                            print("\nInventario vacío.")
                        else:
                            menus.Submenu2()
                            buscar = int(input("Ingrese una opción: "))
                            valor_a_buscar = input("Ingrese valor a buscar: ")

                            resultados = bus.Buscardor(list(Motores_Dic.values()), buscar, valor_a_buscar)

                            if resultados:
                                print("\nResultados de la búsqueda:\n")
                                for producto in resultados:
                                    producto.Mostrar()
                            else:
                                print("No se encontraron productos con ese criterio.")
                    case 4:
                        inven.eliminar()
                    case 5:
                        inven.actualizar()
                    case 6:
                        print("Fin de programa")
                    case _:
                        print("Opcion no valida")
            except ValueError:
                print("Ingrese opcion valida")
            except Exception:
                print(f"Error: {Exception}")

principal = Main()
principal.Main()
Motores_Dic = {}
