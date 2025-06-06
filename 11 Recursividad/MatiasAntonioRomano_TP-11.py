"""1) Crea una función recursiva que calcule el factorial de un número. 
Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario"""

num = int(input("Ingrese un número: "))

def factorial_recursivo(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursivo(num - 1)
    

print(factorial_recursivo(num))

"""2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique."""

pos=int(input("Ingrese una posicion: "))

def fibonacci_recursivo(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)
    
print(fibonacci_recursivo(pos))

"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). 
Prueba esta función en un algoritmo general."""

base = int(input("Ingrese un número base: "))
exponente = int(input("Ingrese un exponente: "))
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

print(potencia_recursiva(base, exponente))

"""4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto."""

n = int(input("Ingresa un número decimal: "))
def decimal_a_binario(n):
    if n == 0:
        return '0'
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
print(decimal_a_binario(n))

"""5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()."""
palabra = str(input("Ingrese una palabra: "))  

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])           

print(es_palindromo(palabra))

"""6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión."""

n = int(input("Ingrese un número entero: "))
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
print(suma_digitos(n))

"""7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente 
hasta llegar al último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide."""

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
print(contar_bloques(5))

"""8) Escribí una función recursiva llamada 
contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número."""

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
print(contar_digito(12345, 1))