#Este programa toma un archivo lee cada una de las lineas de texto
#hace una suma de todos los valores y presenta el resultado en otro
#archivo de texto

#Open permite abirir un archivo
archivoN = open('D:\\Ejercicios programación\\Ejercicios con Python\\EntradaYSalida\\valores.txt', 'rt')
#Si no encuentra el archivo lo crea
archivoS = open('D:\\Ejercicios programación\\Ejercicios con Python\\EntradaYSalida\\valores_totales.txt', 'wt')
print('Proceso entrada')
suma = 0
for linea in archivoN:
    suma += int(linea)
    #imprime el resultado de la linea pero en vez de ejeccutarse en el terminal
    #lo escribe en el archivoS
    print(linea.rstrip(), file=archivoS)
    #imprime el reultado en el convierte el numero a string utilizando str y lo guarda en archivoS
print('\nTotal: ' + str(suma), file=archivoS)
#se cierra el archivo
archivoS.close()
#se muestra un mensaje al usuario en el terminal que la salida esta completa
print('Salida completa')