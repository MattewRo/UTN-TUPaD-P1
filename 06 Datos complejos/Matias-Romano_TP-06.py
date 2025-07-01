"""1) Dado el diccionario 
precios_frutas = {'Banana': 1200, 
'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(f"Punto 1) {precios_frutas}")
print("//////////////////////////")

"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800"""

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(f"Punto 2) {precios_frutas}")
print("//////////////////////////")

"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios."""

lista_frutas = list(precios_frutas)
print(f"Punto 3) {lista_frutas}")
print("//////////////////////////")

"""4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe."""

números_telefónicos = {}

for i in range(5):
    clave_nombre = input(f"Nombre del contacto {i+1}: ")
    valor_número = input(f"Número de contacto {i+1}: ")
    números_telefónicos[clave_nombre] = valor_número
clave = input("Cual es el nombre de la persona a la que deseas llamar: ")
if clave in números_telefónicos:
    print(f"El número de {clave} es: {números_telefónicos[clave]}")
else:
    print(f"No hay un número asociado a {clave}.")

"""5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra."""

frase = input("Ingrese una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")
diccionario_palabras = {}
for palabra in palabras:
    if palabra in diccionario_palabras:
        diccionario_palabras[palabra] += 1
    else:
        diccionario_palabras[palabra] = 1
print(f"Recuento: {diccionario_palabras}")


"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno."""
alumnos={

}

for i in range(3):
    nombre_alumno = input(f"Nombre del alumno {i+1}: ")
    alumnos[nombre_alumno] = ()
    nota1 = float(input(f"Nota 1 del alumno {i+1}: "))
    nota2 = float(input(f"Nota 2 del alumno {i+1}: "))
    nota3 = float(input(f"Nota 3 del alumno {i+1}: "))
    alumnos[nombre_alumno] = alumnos[nombre_alumno] + (nota1, nota2, nota3)
    promedio_alumno = (nota1 + nota2 + nota3) / 3
print(alumnos)
for alumno in alumnos:
    promedio = sum(alumnos[alumno])/len(alumnos[alumno])
    print(f"El promedio del alumno {alumno} es: {promedio}")

"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""
set1 = set(input("Ingrese los estudiantes que aprobaron Parcial 1: ").split())
set2 = set(input("Ingrese los estudiantes que aprobaron Parcial 2: ").split())
set3 = set1.intersection(set2)
set4 = set1.union(set2)
set5 = set1.symmetric_difference(set2)
print(f"Estudiantes que aprobaron ambos parciales: {set3}")
print(f"Estudiantes que aprobaron solo uno de los dos: {set5}")
print(f"Estudiantes que aprobaron al menos un parcial: {set4}")

"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe."""

diccionario_productos = {} 
condicional = True
while condicional == True:
    if input("¿Desea consultar stock de X producto? (s/n): ") == "s":
        producto = input("Ingrese el nombre del producto:")
        if producto in diccionario_productos:
            print(f"El stock del producto {producto} es: {diccionario_productos[producto]}")
    if input("¿Desea agregar un producto? (s/n): ") == "s":
        producto = input("Ingrese el nombre del producto: ")
        unidades = int(input("Ingrese la cantidad de unidades: "))
        diccionario_productos[producto] = unidades
    if input("¿Desea sumar stock a un producto ya existente? (s/n): ") == "s":
        producto = input("Ingrese el nombre del producto: ")
        unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
        if producto in diccionario_productos:
            diccionario_productos[producto] += unidades
        else:
            print("El producto no existe en el inventario.")
    if input("¿Desea realizar otra operación? (s/n): ") == "n":
        condicional = False

"""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Permití consultar qué actividad hay en cierto día y hora."""
agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "15:00"): "Clase de inglés",
    ("Viernes", "21:00"): "Comida con amigos"
}
condicional = True

while condicional == True:
    dia = input(str("Digame el día: "))
    hora = input("Digame la hora en formato HH:MM: ")
    if (dia, hora) in agenda:
        print(f"El evento del día {dia} a las {hora} es: {agenda[(dia, hora)]}")
    else:
        print("No hay eventos programados para ese día y hora.")
    if input("¿Desea realizar otra búsqueda? (s/n): ") == "n":
        condicional = False

"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores."""

original = {"Argentina" : "Buenos Aires", "Chile" : "Santiago", "Brasil" : "Brasilia"}
invertida = {value : key for key, value in original.items()}

print(f"La lista original es {original} y la invertida es {invertida}")