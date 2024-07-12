#Problema 2

#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina.

#1. Ingrese el consumo
consumo = float(input("¿Cuál fue su consumo?"))

#2. Cálculo de la propina 
porcentaje_propina = float(input("¿Qué porcentaje del consumo desea dejar de propina?"))

#3. Resultado

propina = consumo*porcentaje_propina/100

if propina >0:
    print("Gracias por la propina de {}$".format(propina))

else: 
    print("Ingrese un valor válido")

