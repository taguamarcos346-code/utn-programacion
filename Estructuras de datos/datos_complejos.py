# Practico de Datos Complejos 

#Actividad 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadimos las nuevas frutas

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Actividad 2

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# Actualizamos los precios

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Actividad 3

precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

# Creamos la lista de frutas usando las keys del diccionario

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

#Actividad 4

# Creamos un diccionario vacío para almacenar los contactos
contactos = {}

print("¡Vamos a cargar 5 contactos!")

# Bucle para cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
    numero = input(f"Ingresa el número de teléfono de {nombre}: ")
    contactos[nombre] = numero
    print("Contacto guardado.\n")

print("\n--- Tus contactos guardados ---")
print(contactos)
print("-----------------------------\n")

# Pedimos un nombre para buscar
nombre_a_buscar = input("¿De quién quieres buscar el número de teléfono? ")

# Buscamos el número en el diccionario
if nombre_a_buscar in contactos:
    numero_encontrado = contactos[nombre_a_buscar]
    print(f"El número de {nombre_a_buscar} es: {numero_encontrado}")
else:
    print(f"Lo siento, no encontramos a {nombre_a_buscar} en tus contactos.")

#Actividad 5

frase = input("Por favor, ingresa una frase: ")

# Dividimos la frase en palabras y las convertimos a minúsculas para no distinguir entre mayúsculas y minúsculas
palabras = frase.lower().split()

# 1. Usamos un set para obtener las palabras únicas
palabras_unicas = set(palabras)
print("\nPalabras únicas en la frase:")
print(palabras_unicas)

# 2. Creamos un diccionario para contar la frecuencia de cada palabra
conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print("\nCantidad de veces que aparece cada palabra:")
print(conteo_palabras)

#Actividad 6

def calcular_promedios(alumnos_notas):

  promedios = {}
  for alumno, notas in alumnos_notas.items():
    promedio = sum(notas) / len(notas)
    promedios[alumno] = promedio
  return promedios

# Ejemplo de uso:
mis_alumnos = {
    "Sofía": (8, 7, 9),
    "Martín": (6, 5, 7),
    "Valeria": (10, 9, 8)
}

resultados_promedios = calcular_promedios(mis_alumnos)

# Mostramos los resultados
for alumno, promedio in resultados_promedios.items():
  print(f"El promedio de {alumno} es: {promedio:.2f}")

#Actividad 7

# Definimos los sets de estudiantes que aprobaron cada parcial

aprobados_parcial_1 = {"Ana", "Juan", "María", "Pedro", "Lucía"}
aprobados_parcial_2 = {"Juan", "Pedro", "Sofía", "Martín", "Ana"}

print("--- Resultados de los parciales ---")

# 1. Estudiantes que aprobaron ambos parciales (Intersección)

aprobaron_ambos = aprobados_parcial_1.intersection(aprobados_parcial_2)
print(f"\nEstudiantes que aprobaron ambos parciales: {aprobaron_ambos}")

# 2. Estudiantes que aprobaron solo uno de los dos (Diferencia Simétrica)

aprobaron_solo_uno = aprobados_parcial_1.symmetric_difference(aprobados_parcial_2)
print(f"\nEstudiantes que aprobaron solo uno de los dos parciales: {aprobaron_solo_uno}")

# 3. Lista total de estudiantes que aprobaron al menos un parcial (Unión)

aprobaron_al_menos_uno = aprobados_parcial_1.union(aprobados_parcial_2)
print(f"\nLista total de estudiantes que aprobaron al menos un parcial: {aprobaron_al_menos_uno}")

print("\n--- Fin de los resultados ---")

#Actividad 8

def gestionar_stock_simple():
    stock = {
        "Manzanas": 150,
        "Bananas": 200,
        "Naranjas": 120
    }

    while True:
        print("\n--- Menú ---")
        print("1. Consultar stock")
        print("2. Agregar/Modificar stock")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            producto = input("Nombre del producto a consultar: ")
            print(f"Stock de {producto}: {stock.get(producto, 'No encontrado')}")

        elif opcion == '2':
            producto = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad a agregar/establecer: "))
                if cantidad >= 0:
                    stock[producto] = stock.get(producto, 0) + cantidad
                    print(f"Stock de {producto} actualizado a: {stock[producto]}")
                else:
                    print("La cantidad debe ser positiva.")
            except ValueError:
                print("Entrada inválida. Ingresa un número.")

        elif opcion == '3':
            print("¡Adiós!")
            break
        else:
            print("Opción no válida.")

gestionar_stock_simple()

#Actividad 9

def agenda_simple():
    agenda = {}

    while True:
        print("\n--- Agenda ---")
        print("1. Añadir/Modificar evento")
        print("2. Consultar evento")
        print("3. Ver todos")
        print("4. Borrar evento")
        print("5. Salir")

        opcion = input("Elige: ")

        if opcion == '1':
            dia = input("Día: ")
            hora = input("Hora: ")
            evento = input("Evento: ")
            clave = (dia, hora)
            agenda[clave] = evento
            print("¡Guardado!")

        elif opcion == '2':
            dia = input("Día a consultar: ")
            hora = input("Hora a consultar: ")
            clave = (dia, hora)
            print(f"Evento: {agenda.get(clave, 'Nada programado')}")

        elif opcion == '3':
            if not agenda:
                print("Agenda vacía.")
            else:
                print("\n--- Tus Eventos ---")
                for (d, h), ev in sorted(agenda.items()):
                    print(f"[{d} - {h}]: {ev}")
                print("-------------------")

        elif opcion == '4':
            dia = input("Día a borrar: ")
            hora = input("Hora a borrar: ")
            clave = (dia, hora)
            if clave in agenda:
                del agenda[clave]
                print("¡Borrado!")
            else:
                print("No se encontró.")

        elif opcion == '5':
            print("¡Adiós!")
            break
        else:
            print("Opción inválida.")

agenda_simple()

#Actividad 10

def invertir_diccionario_paises(diccionario_original):
   
    diccionario_invertido = {}
    for pais, capital in diccionario_original.items():
        diccionario_invertido[capital] = pais
    return diccionario_invertido

# Ejemplo de uso:
paises_y_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Brasil": "Brasilia",
    "Colombia": "Bogotá"
}

capitales_y_paises = invertir_diccionario_paises(paises_y_capitales)

print("Diccionario original (País: Capital):")
print(paises_y_capitales)
print("\nDiccionario invertido (Capital: País):")
print(capitales_y_paises)
