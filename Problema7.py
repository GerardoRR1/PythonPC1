#Problema 7

#1. Ingrese los números
numero1=float(input("Ingresar primer numero: "))
numero2=float(input("Ingresar segundo numero: "))

#2. Opciones de operaciones 
print("""Elegir entre las 3 opciones
1.Suma de 2 numeros
2.Resta de 2 numeros (primero menos segundo)  
3.Multiplicacion de los 2 numeros""")

#3. Resultado
opcion_elegida=float(input("Ingrese su opcion elegida: "))
if opcion_elegida== 1 :
        resultado=numero1 + numero2
        print("El resultado es {}".format(resultado))

elif opcion_elegida== 2 :
        resultado=numero1 - numero2
        print("El resultado es {}".format(resultado))
    
elif opcion_elegida== 3 :
        resultado=numero1 * numero2
        print("El resultado es {}".format(resultado))
else :
    print("Opcion inválida")