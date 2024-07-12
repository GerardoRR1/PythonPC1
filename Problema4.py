#Problema 4

#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
#pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
#puede ser calculada de la siguiente forma:
#1+2+3+4+.....= n(n+1)/2

#1. Ingrese un número entero positivo
num_sum = int(input("Ingrese un número entero positivo: "))

#2. Fórmula de la sumatoria
sumatoria = num_sum*(num_sum+1)/2

#3. Resultado de la sumatoria
if num_sum < 0:
    print("Ingrese un número positivo")
else:
    print(f"La sumatoria de los enteros positivos hasta N es igual a {sumatoria}")
