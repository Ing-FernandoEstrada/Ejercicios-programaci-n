def validar_fecha(dia, mes):
    meses_con_31_dias = [1, 3, 5, 7, 8, 10, 12]
    meses_con_30_dias = [4, 6, 9, 11]

    if mes < 1 or mes > 12:
        return False

    if mes in meses_con_31_dias:
        return dia >= 1 and dia <= 31
    elif mes in meses_con_30_dias:
        return dia >= 1 and dia <= 30
    elif mes == 2:
        # Validar febrero considerando años bisiestos (29 días) y no bisiestos (28 días)
        if dia >= 1 and dia <= 28:
            return True
        elif dia == 29:
            # Se considera bisiesto si es divisible entre 4 pero no entre 100, o si es divisible entre 400
            return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
        else:
            return False
    else:
        return False


def determinar_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
        return "Aries"
    elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
        return "Géminis"
    elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 23):
        return "Cáncer"
    elif (mes == 7 and dia >= 24) or (mes == 8 and dia <= 23):
        return "Leo"
    elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 23):
        return "Virgo"
    elif (mes == 9 and dia >= 24) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
        return "Escorpio"
    elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
        return "Capricornio"
    elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
        return "Acuario"
    elif (mes == 2 and dia >= 20) or (mes == 3 and dia <= 20):
        return "Piscis"


# Pedir al usuario ingresar el día y mes de nacimiento
dia = int(input("Ingrese el día de su cumpleaños: "))
mes = int(input("Ingrese el mes de su cumpleaños: "))

# Validar la fecha ingresada
if validar_fecha(dia, mes):
    # Determinar el signo zodiacal
    signo = determinar_signo(dia, mes)
    print("Tu signo zodiacal es:", signo)
else:
    print("La fecha ingresada no es válida.")
