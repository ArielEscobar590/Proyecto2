class Producto:
    def __init__(self, id_producto, nombre, precio, id_categoria, total_compras=0, total_ventas=0, stock=0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.id_categoria = id_categoria
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock

class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Ventas:
    pass

class Compras:
    pass

class Empleados:
    pass

class Inventario:
    pass

class Busqueda:
    pass

class Listar:
    pass

class Menus:
    pass

class Clientes:
    pass