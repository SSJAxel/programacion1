
#1 Mostrar los números ascendentes desde el 1 al 10

for numero in range(1, 11):
    print(numero)


#2 Mostrar los números descendentes desde el 10 al 1

for numero in range(10, 0, -1):
    print(numero) 


#3 Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

numero = int(input("ingrese un numero "))
for numero in range(-1, numero):
    numero += 1
    print(numero)


#4 Ingresar un número y mostrar la tabla de multiplicar de ese número.

num = int(input("ingrese un numero "))
result = 0
for numero in range(0, 11):
    result = numero * num
    print(num,"x",numero,"=",result) 


#5 Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0.
#  Mostrar la suma y el promedio de todos los números.

suma = 0
contador = 0

for i in range(10): #aca el maximo de interaciones si:
    numero = int(input(f"ingrese el numero {i + 1}: ")) 
    if numero == 0:
        break #si es 0 corta
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
else:
    promedio = 0
print("promedio de numeros ingresados es", promedio)
print("suma de numeros ingresados", suma) 