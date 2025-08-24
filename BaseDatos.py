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
    pass

class Busqueda:
    pass

class Listar:
    pass

class Modificar:
    pass

class Menus:
    def MenuPrincipal(self):
        print("--Menu principal---")

    def MenuPrincipal2(self):
        print("--Menu principal2---")

