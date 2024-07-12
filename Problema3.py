#Problema 3

#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
#por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
#peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
#cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
#último pedido y calcule el peso total del paquete que será enviado.

#1. Peso de los juguetes
peso_payaso = 112 
peso_muñeca = 75

#2. Cantidad vendida de cada juguete
cantidad_payasos = int(input("Ingrese el número de payasos vendidos: "))
cantidad_muñecas = int(input("Ingrese el número de muñecas vendidas: ")) 

#3. Fórmula del peso final del paquete 
peso_paquete = (cantidad_muñecas*peso_muñeca) + (cantidad_payasos*peso_payaso)

#4. Resultado
print(f"El peso del paquete a enviar es {peso_paquete/1000} kg")