#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla.

nombre = input("Ingrese su nombre por favor: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla.

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = input("Por favor ingrese su edad: ")
lugar_de_residencia = input("Por favor ingrese su lugar de residencia: ")
print(f"Mi nombre es {nombre} {apellido} tengo {edad} años de edad y vivo en {lugar_de_residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 

radio = float(input("Ingrese el valor del radio: "))
pi = float(3.14159)
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El area del circulo ingresado es: {area} y su perimetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale. segs/3600 = horas

segundos = float(input("Ingrese los segundos:"))
formula = segundos / 3600
print(f"el equivalente en horas es: {formula}")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.  

numero = int(input("Ingrese un numero: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese un segundo numero entero: "))
suma = num1 + num2
div = num1 / num2
mult = num1 * num2
rest = num1 - num2
print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la resta es: {rest}")
print(f"El resultado de la multiplicacion es: {mult}")
print(f"El resultado de la division es: {div}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
# modo: imc = peso en kg / (altura en m)**2

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso / (altura)**2
print(f"Su indice de masa corporal es: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
# temp en fhrenheit= 9/5 * celcius + 32

celcius = float(input("Ingrese la temperatura actual: "))
fahrenheit = 9/5 * celcius + 32
print(f"La temperatura en fahrenheit es: {fahrenheit}")

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números. 

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres numeros es: {promedio}")