# Ruta del archivo
ruta = r"D:\Puesto 1\Documents\GitHub\utn-programacion\ManejoDeArchivos\productos.txt"

# Lista donde guardaremos los productos
productos = []

#Leer y cargar productos
with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if not linea:
            continue
        partes = linea.split(",")
        if len(partes) == 3:
            nombre, precio, cantidad = partes
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
        else:
            print(f" Línea con formato incorrecto: {linea}")

# Mostrar los productos cargados
print("Productos cargados:\n")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

#Agregar un nuevo producto

print("\n Agregar nuevo producto:")
nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
productos.append(nuevo_producto)

print("\n Producto agregado a la lista.")

#Buscar producto por nombre

buscar = input("\n Ingrese el nombre de un producto para buscar: ")

# Buscamos en la lista
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar.lower():  # búsqueda sin importar mayúsculas/minúsculas
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\n Producto no encontrado.")

#Guardar productos actualizados
with open(ruta, "w", encoding="utf-8") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\n Archivo productos.txt actualizado correctamente.")


