#Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
#Los datos requeridos son:
#Apellido
#Edad, entre 18 y 90 años inclusive.
#Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
#Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

#Una vez ingresados y validados los datos, mostrarlos por pantalla


#pido apellido
while True:
    apellido = input("Ingrese su apellido: ")
    if apellido:
        break
    print("El apellido no puede estar vacío.")

#validamos edad
while True:
    edad = input("Ingrese su edad (entre 18 y 90 años): ")
    if edad.isnumeric():  # Verifica si es un número positivo
        edad = int(edad)  # Convierte la entrada a entero
        if 18 <= edad <= 90:
            break  # Edad válida, salir del bucle
        else:
            print("La edad debe estar entre 18 y 90 años.")
    else:
        print("Debe ingresar un número válido.")

# Validamos estado civil
estado_civil_permitidos = ["Soltero", "Casado", "Divorciado" , "Viudo" , "Soltera" , "Casada", "Divorciada", "Viuda"]
while True:
    estado_civil = input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a): ").strip().capitalize()
    if estado_civil in estado_civil_permitidos:
        break
    print("Estado civil no válido. Debe ser uno de los siguientes: Soltero/a, Casado/a, Divorciado/a, Viudo/a.")




# Validamos el legajo
while True:
    legajo = input("Ingrese su número de legajo (4 cifras, sin ceros a la izquierda): ")
    if legajo and legajo[0] != '0' and '0000' <= legajo <= '9999':
        legajo = int(legajo)  # Convertir a entero después de validar
        break
    else:
        print("El legajo debe ser un número de 4 cifras, sin ceros a la izquierda.")

#imprimo resultados de los datos solicitados

print("\nDatos ingresados:")
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estado_civil}")
print(f"Número de legajo: {legajo}")
