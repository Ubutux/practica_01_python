"""
En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina.
"""

# Solicitar el consumo en el restaurante
consumo = float(input("Ingrese el consumo en el restaurante: "))

# Solicitar el porcentaje de propina
propina = float(input("Ingrese el porcentaje de propina: "))

# Calcular la cantidad de propina
propina_importe = consumo * propina / 100

# Devolver la cantidad de propina
print("La cantidad de propina a dejar es de", propina_importe)
