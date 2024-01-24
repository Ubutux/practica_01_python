"""
Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.
"""

hora = input("Ingrese la hora: ")

hora_minutos = int(hora.split(":")[0]) * 60 + int(hora.split(":")[1])

if 420 <= hora_minutos <= 480:
    print("Es hora del desayuno")
elif 700 <= hora_minutos <= 780:
    print("Es hora del almuerzo")
elif 1080 <= hora_minutos <= 1140:
    print("Es hora de la cena")
else:
    print("No es hora de comer")

