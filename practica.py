#Problema 1 
#nombre = "Jose"
#def saludo(parámetro):
#    print(f"Hola {parámetro}" )
#saludo(nombre)


#Problema 2
#Escriba un programa que reciba un número entero positivo y devuelva su factorial 
#n = int(input("Ingrese un número : "))

#def factorial(numero):
#    multiplicacion = 1 
#    for i in range (numero):
#        multiplicacion *= i+1
#    print (multiplicacion)

#if n < 0:
#    print(" No se aceptan número negativos")
#else:
#    factorial(n)


#PROBLEMA 4
#Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
#La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver 
#el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

#cantidad = float(input("Ingrese el monto a pagar: "))
#iva = float(input("Ingrese el porcentaje a aplicar: "))

#def monto_total(monto, iva = 21):
#    return ((monto/100)*iva)+monto

#print (f"El monto a pagar es {monto_total(cantidad,iva)}" )
#print (f"El monto a pagar es {monto_total(cantidad)}")


#PROBLEMA 5 
#Escribir una función que calcule el área de un círculo y 
#otra que calcule el volumen de un cilindro usando la primera función.

#import math

#radio = float(input("Ingrese el radio del círculo: "))

#def area_circ(rad):
#    return math.pi* rad**2

#print(f"El área del círculo es {area_circ(radio)}")

#altura = float(input("Ingrese la altura del cilindro: "))

#def vol_cil(area, alt):
#    return area * alt 
#print(f"El volum del cilindro es {vol_cil(area_circ(radio),altura)}")

#opcion2

#radio = float(input("Ingrese el radio del círculo: "))

#def area(rad):
#    return math.pi* rad**2

#def volumen(h):
#    return area(radio)*h

#opera = input("¿Qué operación desea realizar? (1)Calcular área o (2)Calcular volumen?")

#if opera == '1':
#    print(area(radio))
#elif opera == '2':
#    h = float(input("Ingrese la altura: "))
#    print(volumen(h))
#else:
#    print("Ingrese un valor válido")



#PROBLEMA 6
#Escribir una función que reciba una muestra de números en una lista y devuelva su media.
#import math

#n = int(input("Ingrese cuantos números tendrá su lista: "))
#muestras = []
#for i in range(n):
#    muestra = float(input("Escriba la muestra " + str(i+1) + ":"))
#    muestras.append(muestra)

#def media(numeros):
#    total = 0
#    for i in numeros:
#        total += i
#    promedio = total / len(muestras)
#    return promedio

#print("La media es " + str(media(muestras)))


#PROBLEMA 7
#Escribir una función que reciba una muestra de 
#números en una lista y devuelva otra lista con sus cuadrados.

n = int(input("Ingrese el número de elementos: "))

lista_norm = []
for i in range(n):
    elemento = float(input("Ingrese el elemento " + str(i+1) + ":"))
    lista_norm.append(elemento)

def lista_cuadr(numeros):
    cuadrados = []
    for i in numeros:
        cuadrado = i**2
        cuadrados.append(cuadrado)
    return cuadrados

print("La lista elevada al cuadrado es " + str(lista_cuadr(lista_norm)))