"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea"""


for i1 in range(0,101):
    print(f"{i1}")

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

num = int(input("Ingrese su numero: "))
i2 = 0
while num > 0:
    num = num // 10
    i2 += 1
print(f"El numero tiene {i2} digitos")

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = 0
for i in range (num1, num2+1):
    num3+=i
print(f"La suma de todos los numero enteros comprendidos entre los numeros es {num3}")

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0"""
n = int(input("Ingrese el primer numero a sumar: "))
suma = 0

while n > 0:
    suma += n
    n = int(input("Ingrese otro numero o 0 para decir la suma: "))
print(f"La suma total de todos los numeros es {suma}")

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
from random import randint

num_ale = randint(0,9)

num = int(input("Dime un numero de 0 al 9 para ver si aciertas: "))
intent = 1

while num != num_ale:
    intent += 1
    num = int(input("Dime un numero de 0 al 9 para ver si aciertas: "))
print(f"El numero aleatorio era {num_ale} y lo adivinaste en {intent} intentos.")

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente."""

