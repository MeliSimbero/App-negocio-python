# crear funciones para interfaz consola
from clases import clientes, producto, venta, inventario
from clases.mascotas import gato, perro
from clases.inventario import inventario
from clases.clientes import cliente
from clases.producto import productos
from clases.venta import ventas


def registrar_mascota():
    tipo = input("Por favor indicar tipo de mascota: perro o gato. ").strip().lower()
    nombre = input("Ingres el nombre de la mascota: ").lower()
    edad = int(input("Ingrese la edad de la mascota en años: "))
    salud = input("Estado de salud de la mascota: ")
    precio = float(input("Precio de la mascota: "))

    if tipo == "perro":
        raza = input("Raza del perro: ")
        nivel_energia = input("Nivel de energía del perro:  ")
        mascota = perro(nombre, edad, salud, precio, raza, nivel_energia)
    elif tipo == "gato":
        raza = input("Raza del gato: ")
        independencia = input("Nivel de independencia del gato: ")
        mascota = gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print("Tipo de mascota no reconocido.")
        return
    return mascota

def registrar_cliente():
    nombre = input("Ingrese nombre del cliente: ")
    direccion = input("Ingrese direccion del cliente: ")
    telefono = int(input("Ingrese telefono del cliente: "))
    client = cliente(nombre, direccion, telefono)
    return client

def registrar_producto():
    nombre = input("Ingrese nombre del producto: ")
    categoria = input("Ingrese categoria del producto: ")
    precio = float(input("Ingrese precio del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))
    producto = productos(nombre, categoria, precio, cantidad)
    return producto

def registrar_venta(cliente, inventario):
    nombre_cliente = input("Ingrese nombre del cliente: ")
    cliente = next((c for c in cliente if c.nombre == nombre_cliente), None) #metodo que devuelve una instancia
    if not cliente:
        print("Cliente no encontrado")
        return 

    productos = []
    while True: #True para que sea bucle constante, se usa break para salir.
        nombre_producto = input("Nombre del producto (deje vacio para finalizar): ")
        if not nombre_producto:
            break
        producto = next((p for p in inventario.lista_de_productos if p.nombre == nombre_producto), None)
        if producto:
            productos.append(producto)
        else: print("Producto no encontrado.")
    if productos:
        venta = ventas(cliente, productos)
        venta.registrar_venta()
        print("La venta se ha registrado correctamente.")
    else:
        print("No se registro ninguna venta.")

def mostrar_menu():
    print("\n --- Menú Patas Felices ---" )
    print("1. Registrar mascota.")
    print("2. Registrar cliente.")
    print("3. Registrar producto.")
    print("4. Registrar venta.")
    print("5. Mostrar informacion de: Mascotas.")
    print("6. Mostrar informacion de: Clientes.")
    print("7. Mostrar informacion de: Productos.")
    print("8. Generar alerta de inventario.")
    print("9. Salir.")

def main():
    mascotas = []
    clientes = []
    sumar_inventario = inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            mascota = registrar_mascota()
            if mascota: 
                mascotas.append(mascota)
                print(f"{mascota.nombre} registrada con exito!")
        elif opcion == "2":
            cliente = registrar_cliente()
            if cliente: 
                clientes.append(cliente)
                print(f"{cliente.nombre} registrada con exito!")
        elif opcion == "3":
            producto = registrar_producto()
            if producto: 
                sumar_inventario.agregar_producto(producto)
                print(f"{producto.nombre} registrado con exito!")
        elif opcion == "4":
            nueva_venta = registrar_venta(clientes, sumar_inventario)
            if nueva_venta:
                print(f"La venta de {nueva_venta.cliente.nombre} fue registrada con exito!")
        elif opcion == "5":
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota, perro) or isinstance(mascota, gato):
                    print(mascota.mostrar_caracteristicas())
        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrar_informacion())
        elif opcion == "7":
            for producto in sumar_inventario.lista_de_productos:
                print(producto.mostrar_informacion())
        elif opcion == "8":
            umbral_minimo = int(input("Ingrese el stock minimo del producto: "))
            print(sumar_inventario.alerta_stock(umbral_minimo))
        elif opcion == "9":
            print("Salió del sistema. Gracias por confiar en nosotros.")
        else:
            print("Opcion no valida. Seleccione una opcion del 1 al 9: ")
if __name__ == "__main__":
    main()
