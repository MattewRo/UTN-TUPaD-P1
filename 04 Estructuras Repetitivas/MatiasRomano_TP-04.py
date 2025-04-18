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