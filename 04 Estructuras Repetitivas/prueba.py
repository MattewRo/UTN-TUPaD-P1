numm = int(input("Ingresa el numero:"))
numm_rev = 0
while numm != 0:
    digito = numm % 10
    numm_rev = numm_rev * 10 + digito
    numm = numm // 10
print(f"El numero invertido de {numm} es {numm_rev}") 