import re

codigo_cinco_digitos = '12345'
codigo_nueve_digitos = '12345-6789'
numero_telefono = '123-456-789'

# El modulo ayuda a hacer la busqueda con expresiones regulares
#ayuda a encontrar grupos de 5 numeros

# Esta expresion define un patron para encontrar numeros de 5 digitos
regex_cinco_numeros = r'\d{5}'

#
print(re.search(regex_cinco_numeros, codigo_cinco_digitos))
print(re.search(regex_cinco_numeros, codigo_nueve_digitos))
print(re.search(regex_cinco_numeros, numero_telefono))