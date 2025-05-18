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