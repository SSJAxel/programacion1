#Ingresar un número. Mostrar todos los divisores que hay 
# desde el 1 hasta el número ingresado.
#Mostrar la cantidad de divisores encontrados.
num = int(input("ingrese un numero: "))
contador = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        contador += 1