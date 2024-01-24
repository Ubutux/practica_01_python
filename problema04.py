"""
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
puede ser calculada de la siguiente forma:
1+2+3+ ... + n = n(n+1)/2
"""
# Solicitar al usuario el número N
n = int(input("Ingrese un número positivo: "))

# Calcular la suma de los N primeros enteros positivos
suma = n * (n + 1) // 2

# Devolver la suma
print("La suma de los", n, "primeros enteros positivos es de", suma)
