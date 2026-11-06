def ecuacion2(a, b, c):

    if a == 0:
        raise ValueError("El coeficiente a no puede ser cero")

    import math

    discriminante = b ** 2 - 4 * a * c

    if discriminante == 0:
        x = -b / (2 * a)
        return (x, x)

    elif discriminante < 0:
        print("no hay solucion")

    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)

        return (x1, x2)