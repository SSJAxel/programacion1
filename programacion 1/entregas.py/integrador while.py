#Realizar un programa que permita que el usuario ingrese todos los números
#que desee. Una vez finalizada la carga determinar:
#La suma acumulada de los números negativos.
#La suma acumulada de los números positivos.
#La cantidad de números negativos ingresados.
#El promedio de los números positivos.
#El número positivo más grande.
#El porcentaje de números negativos ingresados, respecto del total de ingresos.

#de momento las declaro asi, pero es para que se entienda, suelo entenderme mejor
#con variables de 2/3 letras y comentar al lado de declararlas que significan
#para una lectura mas rapida, simplemente un gusto personal

negativos = 0
positivos = 0
total_negativos = 0
total_positivos = 0
total_numeros = 0
maximo_positivo = None

#empiezo con el programa

while True:
    numero = int(input("ingrese un numero (para dejar de ingresar numeros escriba 000 para terminar)"))
    if numero == 000:
        break

    if numero < 0:
        negativos += 1
        total_negativos += 1
    elif numero > 0:
        positivos += 1
        total_positivos += 1
    if maximo_positivo is None or numero > maximo_positivo:
        maximo_positivo = numero
    total_numeros += 1

    if total_positivos > 0:
     promedio_positivo = positivos / total_positivos
    else:
        promedio_positivo = 0

    if total_numeros > 0:
     porcentaje_negativo = (total_negativos / total_numeros) * 100
    else:
        porcentaje_negativo = 0

print("Suma acumulada de números negativos:", negativos )
print("Suma acumulada de números positivos:", positivos)
print("Cantidad de números negativos ingresados:", total_negativos)
print("Promedio de números positivos:", promedio_positivo)
print("Número positivo más grande:", maximo_positivo)
print("Porcentaje de números negativos:", porcentaje_negativo, "%")

#hice las variables largas y legibles. pero yo me guardo una copia a mi estilo para mas comodidad, creo haber tardado mas por solo elegir 
#nombres largos

