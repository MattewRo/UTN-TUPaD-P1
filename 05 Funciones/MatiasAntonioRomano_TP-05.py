import TP05_utils

"""1 Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

TP05_utils.imprimir_hola_mundo()

"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""

TP05_utils.saludar_usuario(nombre=str(input("Dime tu nombre: ")))

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados."""
TP05_utils.informacion_personal(str(input("Ingrese el nombre: " )), str(input("Ingrese el apellido: ")), int(input("Ingrese la edad: ")), str(input("Ingrese la residencia: ")))

"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""

radio = int(input("Ingrese el radio del círculo: "))
TP05_utils.calcular_area_circulo(radio)
TP05_utils.calcular_perimetro_circulo(radio)

"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función."""

segundos = int(input("Ingrese la cantidad de segundos: "))
TP05_utils.segundos_a_horas(segundos)

"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""

numero = int(input("Ingrese el número: "))
TP05_utils.tabla_multiplicar(numero)

"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
TP05_utils.operaciones_basicas(a, b)

"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales."""

peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))
TP05_utils.calcular_imc(peso, altura)

"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
TP05_utils.celsius_a_fahrenheit(celsius)

"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""

num1=int(input("Ingrese el numero 1: "))
num2=int(input("Ingrese el numero 2: "))
num3=int(input("Ingrese el numero 3: "))
TP05_utils.calcular_promedio(num1, num2, num3)