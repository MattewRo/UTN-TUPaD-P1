from random import randint
num_ale = randint(0,9)

num = int(input("Dime un numero de 0 al 9 para ver si aciertas: "))
intent = 1

while num != num_ale:
    intent += 1
    num = int(input("Dime un numero de 0 al 9 para ver si aciertas: "))
print(f"El numero aleatorio era {num_ale} y lo adivinaste en {intent} intentos.")