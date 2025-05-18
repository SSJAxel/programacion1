#Ingresar un número. Mostrar cada número primo
#que hay entre el 1 y el número ingresado.
#Informar cuántos números primos se encontraron.

num = int(input("ingrese un numero: "))
contadordeprimos = 0
for i in range(2, num + 1):
    esprimo = True
    for j in range(2,i):
        if i % j == 0:
            esprimo = False
            break
    if esprimo:
        print(i)
        contadordeprimos += 1
print(f"Se encontraron {contadordeprimos} números primos.")