"""
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.
"""

numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))

opciones = {
    1: "Suma",
    2: "Resta",
    3: "Multiplicación"
}

opcion = int(input("¿Qué operación desea realizar?\n"
                      "1. Suma\n"
                      "2. Resta\n"
                      "3. Multiplicación\n"
                      "Seleccione una opción: "))
operacion = opciones[opcion]
if opcion == 1:
    resultado = numero_1 + numero_2
elif opcion == 2:
    resultado = numero_1 - numero_2
elif opcion == 3:
    resultado = numero_1 * numero_2

print("El resultado de la operación", operacion, "es", resultado)


