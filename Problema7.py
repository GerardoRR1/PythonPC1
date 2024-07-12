#Problema 7:
#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- En caso de introducir una opción inválida, el programa informará de que no es correcta.

#1. Ingrese los números
num_prim  = float(input("Introduce el primer número: "))
num_seg  = float(input("Introduce el segundo número: "))

#2. Cálculos
suma_nums = num_prim+num_seg
rest_nums = num_prim-num_seg
mult_nums = num_prim*num_seg

if suma_nums and rest_nums and mult_nums == float:
print("""El resultado de la suma es {}, el resultado de la resta es {} y el resultado de la multiplicación 
es {}""".format(suma_nums,rest_nums,mult_nums))
