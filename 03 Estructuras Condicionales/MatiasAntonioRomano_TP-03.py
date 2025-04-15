#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”
EDAD_MAYOR_MINIMA = 18;
edad = int(input("Escriba su edad: "))

if edad >= EDAD_MAYOR_MINIMA:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
NOTA_MINIMA_APROBADA = 6
nota = float(input("Escriba su nota: "))

if nota >= NOTA_MINIMA_APROBADA:
    print("Aprobado.")
else:
    print("Desaprobado.")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
num = int(input("Ingrese un numero: "))

if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.
edad2 = int(input("Ingrese su edad: "))

niño = bool(edad2 < 12)
adol = bool(edad2 >= 12 and edad2 < 18)
adul = bool(edad2 >= 18 and edad2 < 30)
adulmay = bool (edad2 >= 30)

#Coloque este if para que el usuario no pueda escribir un numero negativo y pida un num positivo
if edad2 > 0:
    if niño == True:
        print("Pertenece a la categoria Niño/a.")
    elif adol == True:
        print("Pertenece a la categoria Adolescente.")
    elif adul == True:
        print("Pertenece a la categoria Adulto.")
    else:
        print("Pertenece a la categoria Adulto mayor.")
else:
    print("Porfavor escriba un numero positivo.")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contra = input("Escriba una contraseña: ")

if len(contra) >= 8 and len(contra) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mode, median, mean 

numeros_aleatorios = (random.randint(1, 100) for i in range (50))

mode(numeros_aleatorios)
median(numeros_aleatorios)
mean(numeros_aleatorios)

sesg_pos = bool(mean > median > mode)
sesg_neg = bool(mean < median < mode)
sesg_0 = bool(mean == median == mode)

if sesg_pos == True:
    print(f"La mediana, media y moda en orden son: {mean}, {median} y {mode}; Y estas tiene el sesgo positivo.")
elif sesg_neg == True:
    print(f"La mediana, media y moda en orden son: {mean}, {median} y {mode}; Y estas tiene el sesgo negativo.")
else:
    print(f"La mediana, media y moda en orden son: {mean}, {median} y {mode}; Y no tienen sesgo.")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

palabra = input("Escribe la palabra a continuacion: ")

vocal = ("a"), ("o"), ("e"), ("i"), ("u"), ("A"), ("O"), ("E"), ("I"), ("U")

if palabra.endswith(vocal):
    print(f"{palabra}!")
else:
    print(f"{palabra}")

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.""" 
print("Ingrese un numero para las siguientes opciones: 1.Su nombre en mayúsculas. 2. Su nombre en minúsculas. 3.Su nombre con la primera letra mayúscula.")
opcion = int(input())
nombre =input("Ingrese su nombre a continuacion: ")

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("No seleccionaste una de las 3 opciones.")

"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por 
pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""
magnitud = int(input("Escriba la magnitud del terremoto: "))

mag_mleve = bool(magnitud < 3)
mag_leve = bool(magnitud >= 3 and magnitud < 4)
mag_mode = bool(magnitud >= 4 and magnitud < 5)
mag_fuerte = bool(magnitud >= 5 and magnitud < 6)
mag_mfuerte = bool(magnitud >= 6 and magnitud < 7)
mag_extremo = bool(magnitud >= 7)

if magnitud > 0:
    if mag_mleve == True:
        print("La magnitud de su terremoto es muy leve.")
    elif mag_leve == True:
        print("La magnitud de su terremoto es leve.")
    elif mag_mode == True:
        print("La magnitud de su terremoto es moderada.")
    elif mag_fuerte == True:
        print("La magnitud de su terremoto es fuerte.")
    elif mag_mfuerte == True:
        print("La magnitud de su terremoto es muy fuerte.")
    elif mag_extremo == True:
        print("La magnitud de su terremoto es extrema.")
else:
    print("Magnitud negativa inexistente, favor de colocar una magnitud correcta.")

"""10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano."""

#Se declaran primeras variables que seran introducidas por el usuario y se realiza el input
hemisferio = str(input("Dime de que hemisferio eres (N/S):  "))
mes = int(input("Dime que mes es: "))
dia = int(input("Dime que dia es: "))

#Genero boleanos para que se haga mas comodo dentro del if
mes1_2 = bool(mes == 1 or mes == 2)
mes4_5 = bool(mes == 4 or mes == 5)
mes7_8 = bool(mes == 7 or mes == 8)
mes10_11 = bool(mes == 10 or mes == 11)


if (dia <= 31 and dia >= 1) and (mes <= 12 and mes >= 1): #if para que el usuario solo pueda escribir dias del 1 al 31 y meses del 1 al 12
    if hemisferio == "N" or hemisferio == "S": #Lo mismo pero para que solo pueda escoger entre N y S
        if hemisferio == "N": #if general para cuando sea hemisfero N
            if (mes == 12 and dia >= 21) or mes1_2 == True or (mes == 3 and dia <= 20):
                print("Usted se encuentra en Invierno.")
            elif (mes == 3 and dia >= 21) or mes4_5 == True or (mes == 6 and dia <=20):
                print("Usted se encuentra en Primavera.")
            elif (mes == 6 and dia >= 21) or mes7_8 == True or (mes == 9 and dia <=20):
                print("Usted se encuentra en Verano.")
            elif (mes == 9 and dia >= 21) or mes10_11 == True or (mes == 12 and dia <=20):
                print("Usted se encuentra en Otoño.")
        elif hemisferio == "S":#if general para cuando sea emisfero S
            if (mes == 12 and dia >= 21) or mes1_2 == True or (mes == 3 and dia <= 20):
                print("Usted se encuentra en Verano.")
            elif (mes == 3 and dia >= 21) or mes4_5 == True or (mes == 6 and dia <=20):
                print("Usted se encuentra en Otoño.")
            elif (mes == 6 and dia >= 21) or mes7_8 == True or (mes == 9 and dia <=20):
                print("Usted se encuentra en Invierno.")
            elif (mes == 9 and dia >= 21) or mes10_11 == True or (mes == 12 and dia <=20):
                print("Usted se encuentra en Primavera.")
    else: #ELse para cuando no escribe bien el emisferio
        print("No haz escrito el hemisferio correcto (Recuerda escribirlo en mayúscula).")
else: #Else para cuando coloca una fecha fuera de lo permitido
    print("Haz colocado una fecha no existente.")

