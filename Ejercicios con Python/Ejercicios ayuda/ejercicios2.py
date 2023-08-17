import math

def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        # Dos soluciones diferentes
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        # Solución única
        x = -b / (2 * a)
        return x
    else:
        # Sin soluciones reales
        return None

# Solicitar los coeficientes de la ecuación
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Resolver la ecuación de segundo grado
solution = solve_quadratic_equation(a, b, c)

# Mostrar la solución
if solution is None:
    print("La ecuación no tiene soluciones reales.")
elif isinstance(solution, tuple):
    x1, x2 = solution
    print("Las soluciones son:")
    print("x1 =", x1)
    print("x2 =", x2)
else:
    print("La solución única es:")
    print("x =", solution)