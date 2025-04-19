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