#1)
num=0
while num<10:
    num+=1
    print(num)

#2)
num=10
while num>0:
    print(num)
    num-=1
#3)
num=0
acum=0
while num<10:
    num+=1
    acum+=num
    print(acum)
#4)
num=0
acum=0
while num<10:
    num+=2
    acum+=num
    print(acum)
#5)
num=0
acum=0
count=1
while count<=5:

    num=int(input("ingrese el numero: "))
    acum+=num
    count+=1

prom=acum/count
print(f"la suma es {acum} y el promedio es {prom}")
#6)
num:0
continuar=True
acum=0
prom=0
cant=0
while continuar:
    cant+=1
    num=int(input(f"ingrse su numero {cant}: "))
    acum+=num
    rta=input("usted desea continuar S | N: ")
    while rta != "S" and rta!= "N" and rta != "s" and rta != "n":
        rta=input("valor incorrecto porfavor volver a ingresar S | N: ")
    if rta =="N" or rta =="n":
        continuar=False
prom=acum/cant
print(f"la suma de sus {cant} numeros es {acum} y el promedio es {prom}")
#7)
producto_numerico = 1
suma_numerica = 0
continuacion = None

while True:
    numero = input("Ingrese un numero: ")
    if int(numero) < 0:
        producto_numerico = int(numero) * producto_numerico
    else:
        suma_numerica = int(numero) + suma_numerica

    continuacion = input("Desea continuar? S ! N: ")
    while continuacion != "S" and continuacion != "N" and continuacion != "s" and continuacion != "n":
        continuacion = input("ERROR. Desea continuar? S ! N: ")
    
    if continuacion == "N" or continuacion == "n":
        break


print(f"El producto es: {producto_numerico}")
print(f"La suma es: {suma_numerica}")
#8)
num=0
maxi=None
cont=10
mini=None
while cont:
    num=int(input(f"ingrese su numero {cont}: "))
    cont-=1
    if maxi is None and mini is None:  
        maxi = num  
        mini = num  
    if num>maxi:
        maxi=num
    elif num<mini:
        mini=num
print(f"el maximo es {maxi} y el minimo es {mini}")
#9)
num:0
continuar=True
acum=0
prom=0
cant=0
while continuar:
    cant+=1
    num=int(input(f"ingrse su numero {cant}: "))
    acum+=num
    rta=input("usted desea continuar S | N: ")
    
    while rta != "S" and rta!= "N" and rta != "s" and rta != "n":
        rta=input("valor incorrecto porfavor volver a ingresar S | N: ")
    if rta =="N" or rta =="n" and cant>=5:
        continuar=False
    elif cant<5:
        print("minimo ingresar 5 numeros")
prom=acum/cant
print(f"la suma de sus {cant} numeros es {acum} y el promedio es {prom}")

#10)
num:0
continuar=True
acum=0
prom=0
cant=0
while continuar:
    cant+=1
    num=int(input(f"ingrse su numero {cant}: "))
    acum+=num
    rta=input("usted desea continuar S | N: ")
    
    while rta != "S" and rta!= "N" and rta != "s" and rta != "n":
        rta=input("valor incorrecto porfavor volver a ingresar S | N: ")
    if rta =="N" or rta =="n" and cant>=5:
        continuar=False
    elif cant<5:
        print("minimo ingresar 5 numeros")
    elif cant>=10:
        print("maximo igresar 10 numeros")
        continuar=False
prom=acum/cant
print(f"la suma de sus {cant} numeros es {acum} y el promedio es {prom}")

# integrador del while 
positivos=0
negativos=0
num=0
pos_sum=0
neg_sum=0
pos_prom=0
neg_percent=0
pos_max=0
cant=0
continuar=True
while continuar:
    cant+=1
    num=int(input(f"ingrese un numero {cant}: "))
    if num>=0:
        pos_sum+=num
        positivos+=1
        if num>pos_max:
            pos_max=num
    else:
        neg_sum+=num
        negativos+=1
    
    rta=input("usted desea continuar S | N: ")
    while rta != "S" and rta!= "N" and rta != "s" and rta != "n":
        rta=input("valor incorrecto porfavor volver a ingresar S | N: ")
    if rta =="N" or rta =="n":
        continuar=False
pos_prom=pos_sum/positivos
neg_percent=(negativos*100)/cant
print(f"La suma acumulada de los números negativos es: {neg_sum} \n La suma acumulada de los números positivos es: {pos_sum}\n La cantidad de números negativos ingresados es: {negativos}\n El promedio de los números positivos es : {pos_prom}\n El número positivo más grande es: {pos_max}\n El porcentaje de números negativos ingresados, respecto del total de ingresos es: {neg_percent}")

validaciones
#voy a tomar en cuenta que existe una contraseña ya creada para estos ejemplos y la cual va a ser 8m?7D
#1)

password = "8m?7D"

ingreso=input("ingrese su contraseña: ")
if password != ingreso:
    while password != ingreso:
        ingreso=input("su contraseña es incorrecta porfavor volver a intentar: ")
print("contraseña correcta wellcum")

#2)
password = "8m?7D"
intentos=1

ingreso=input("ingrese su contraseña: ")
if password != ingreso:
    while password != ingreso and intentos<5:
        ingreso=input("su contraseña es incorrecta porfavor volver a intentar: ")
        print(f"le quedan {5-intentos} ")
        intentos+=1
    if  password != ingreso:
        print("intentos acabados se le bloqueara la cuenta")
        exit()
print("contraseña correcta wellcum")
#3)
nota=None
nota=int(input("ingrese la nota: "))
while nota<1 or nota>10:
    nota=int(input("nota fuera de rango volver a ingresar"))
print(f"su nota es {nota}")

#4)
color=None
color=str(input("ingrese un color entre rojo,verde o azul: ")).upper()

while color != "ROJO" and color != "VERDE" and color != "AZUL":
    color=str(input("color erroneo volver a ingresar: ")).upper()
print(f"su color es {color.title()}")

#integrador de verificacion)    

import re        
patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\- ]{2,50}$'
apellido=""
edad=None
estado_civil=""
num_legajo=None
apellido=input("ingrese apellido: ")
while True:
    if re.match(patron, apellido):
        print("apellido valido")
        break
    else:
        apellido=input("apellido invalido volver a intentar: ")
edad=int(input("igrese su edad: "))
while edad<18 or edad>90:
    edad=int(input("edad fuera del limite ingresar devulta: "))
estado_civil=input("ingrese su estado civil Soltero/a | Casado/a | Divorciado/a | Viudo/a: " ).upper()
while  estado_civil != "SOLTERO" and estado_civil != "CASADO" and estado_civil !="DIVORCIADO" and estado_civil != "VIUDO" and  estado_civil != "SOLTERA" and estado_civil != "CASADA" and estado_civil !="DIVORCIADA" and estado_civil != "VIUDA":
    estado_civil=input("error al ingresar su estado civil porfavor intente devuelta Soltero/a | Casado/a | Divorciado/a | Viudo/a: ").upper()
num_legajo=int(input("ingrese su numero de legajo: "))
while num_legajo<1000 or num_legajo>9999:
    num_legajo=int(input("su numero de legajo no no existe porfavor volver a ingresar: "))        
print(f"su apellido es {apellido} su estado civil es {estado_civil.title()} su edad es {edad} su numero de legajo es {num_legajo}")
