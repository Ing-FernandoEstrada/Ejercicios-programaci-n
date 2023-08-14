numero = int(input("Ingrese un número entero entre 0 y 9999: "))

# Verificar que el número esté dentro del rango permitido
if numero < 0 or numero > 9999:
    print("El número ingresado está fuera del rango permitido.")
else:
    # Convertir el número en una cadena y revertir la cadena
    numero_revertido = str(numero)[::-1]

    # Mostrar el número invertido
    print("El número invertido es:", numero_revertido)