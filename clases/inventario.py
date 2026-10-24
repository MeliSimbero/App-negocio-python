class inventario:
    def __init__(self):
        self.lista_de_productos = []
    def agregar_producto(self, producto):
        self.lista_de_productos.append(producto)
    def actualizar_inventario(self, producto, cantidad):
        for prod in self.lista_de_productos:
            if prod.nombre == producto.nombre:
                prod.actualizar_cantidad(cantidad)
    def alerta_stock(self, umbral_minimo):
        alerta = [prod.nombre for prod in self.lista_de_productos if prod.cantidad < umbral_minimo]
        return f"Productos por debajo del stock necesario: {', '.join(alerta)}" if alerta else "Stock ok."
        umbral_minimo <= 2