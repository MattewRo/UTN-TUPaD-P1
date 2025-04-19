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
for i in range (num1+1, num2):
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

for i in range (100, -1, -2):
    print(f"{i}")

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario."""

n_1 = int(input("Ingrese el numero entero: "))
n_f = 0
for i in range (0, n_1+1):
    n_f+=i
print(f"La suma de todos los numero enteros comprendidos entre 0 y tu numero es {n_f}")

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""
num_imp = 0
num_par=0
num_pos=0
num_neg=0

n__1 = 0

for i in range (0, 100):
    n__1 = int(input("Ingrese el numero: "))
    if n__1 % 2 == 0 and n__1 > 0:
        num_par += 1
        num_pos += 1
    elif n__1 % 2 == 0 and n__1 < 0:
        num_par += 1
        num_neg += 1
    elif n__1 % 2 != 0 and n__1 > 0:
        num_imp += 1
        num_pos += 1
    elif n__1% 2 != 0 and n__1 < 0:
        num_imp += 1
        num_neg += 1

print(f"La cantidad de numeros pares es {num_par}, los numeros impares fueron {num_imp}, los numeros positivos fueron {num_pos} y los numeros negativos fueron {num_neg}")

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""