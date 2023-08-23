#Las pruebas unitarias sirvben para ir corrigiendo el codigo teniendo en cuenta
#que se debe verificar probando con preguntas y segun los resultados se ve que
#tan bien esta escrito el codigo
def verificar_temp(temp):
    if temp < 15:
        print('Usa un abrigo y bufanda')
    elif temp >= 25 and temp <= 35:
        print("Usa un abrigo")
    elif temp > 35:
        print('Deja el abrigo en casa')

verificar_temp(10)
verificar_temp(30)
verificar_temp(37)