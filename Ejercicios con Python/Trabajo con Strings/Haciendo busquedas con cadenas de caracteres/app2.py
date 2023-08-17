primernombre = 'edgar'
segundonombre = 'fernando'
premio='Ganador premio de programación'

#La funcione permite para que la primer letra se convierta en mayuscula
primer_nombre_cap = primernombre.capitalize()
segundo_nombre_cap = segundonombre.capitalize()

#El metodo find permite buscar una palabra en una cadena de caracteres
premio_ubicacion = premio.find('premio')

#Ejemplo para realizar una substracición en una cadena de caracteres
premio_texto = premio[8:]

print(primer_nombre_cap)
print(segundo_nombre_cap)
print(premio_ubicacion)
print(premio_texto)