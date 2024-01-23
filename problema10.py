"""
Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
encuentran en la posición 0, 4 y 5.
lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
Resultado esperado: ['Verde', 'Blanco', 'Negro']
"""

colores=["Rojo", "Verde", "Blanco", "Negro", "Rosa", "Amarillo"]

print(colores)
colores.remove("Rojo")
colores.remove("Rosa")
colores.remove("Amarillo")

print(colores)
