class productos:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad #setter que va actualizando cantidad
    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Categoria: {self.categoria}, Precio: ${self.precio}, Cantidad: {self.cantidad}"
    