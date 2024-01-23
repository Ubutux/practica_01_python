"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.
"""

# Declaramos las variables
payasos = int(input("Ingrese el número de payasos vendidos: "))
muñecas = int(input("Ingrese el número de muñecas vendidas: "))

# Calcular el peso de los payasos
peso_payasos = payasos * 112

# Calcular el peso de las muñecas
peso_muñecas = muñecas * 75

# Sumar el peso de los payasos y el peso de las muñecas
peso_total = peso_payasos + peso_muñecas

# Devolver el peso total del paquete
print("El peso total del paquete es de", peso_total, "g")
