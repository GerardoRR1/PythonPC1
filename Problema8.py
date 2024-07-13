#Problema 8:

#Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
#entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
#Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
#hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
#Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
#suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
#las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.

def obtener_momento_comida(hora):
    # Convertir la hora a formato de 24 horas y convertirlo a float
    horas, minutos = map(int, hora.split(':'))
    hora_float = horas + minutos / 60.0
    
    # Definir los rangos para cada comida
    if 7 <= hora_float <= 8:
        return "Es la hora del desayuno."
    elif 12 <= hora_float <= 13:
        return "Es la hora del almuerzo."
    elif 18 <= hora_float <= 19:
        return "Es la hora de la cena."
    else:
        return None

# Solicitar la entrada del usuario
hora_usuario = input("Ingrese la hora en formato 24 horas: ")

# Obtener el momento de la comida y mostrar el resultado
momento_comida = obtener_momento_comida(hora_usuario)
if momento_comida:
    print(momento_comida)
