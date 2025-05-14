#Definicion de funciones
#1
def imprimir_hola_mundo():
    print("Hola, mundo!")
#2
def saludar_usuario(nombre):
    print(f"Hola, {nombre}")
#3
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#4
def calcular_area_circulo(radio):
    area = 3.14159 * (radio ** 2)
    print(f"El area es de: {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14159 * radio
    print(f"El perimetro es de: {perimetro}")
#5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"El tiempo es de: {horas} horas")
#6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
#7
def operaciones_basicas(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
#8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu IMC es de: {imc}")
#9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"La temperatura en fahrenheit es de: {fahrenheit}")
#10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio es de: {promedio}")
