#Esto es una cadena de caracteres la cual se debe convertir a un número
radio=input('Ingrese el valor del radio del circulo')
#area_circulo = (valor_radio ** 2) * 3.14159
print(radio + ' Es el valor del radio del circulo')
#De esta manera se permite convertir la cadena de caracteres a un numero que este caso va
#va a hacer de ripo decimal
valor_radio = float(radio)
area_circulo = (valor_radio ** 2) * 3.14159
print('El area del resultado es: ')
print(area_circulo)

area=input('Ingrese el valor del area')
altura=input('Ingrese el valor de la altura')
valor_area = float(area)
valor_altura = float(altura)
area_tringulo = (valor_area*valor_altura)/2
print('El valor del area del tringulo es: ' )
print(area_tringulo)

def calcular_area_cuadrado(lado):
    calcular = lado**2
    return calcular

lado = float(input('Digite la longitud del cuadrado'))
calcular_area = calcular_area_cuadrado(lado)
print(f"El resultado del area del cuadrado es: {calcular_area}")