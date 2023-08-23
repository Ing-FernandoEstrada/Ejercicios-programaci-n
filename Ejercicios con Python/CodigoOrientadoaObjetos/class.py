#Se utiliza la palabra class para declarar una clase que tiene varias declaraciones
class Invitado:
    'Clase comun para todos los invitados'

# Este es el metodo constructor y es el primer metodo que se ejecuta cuando se crea la instancia de la clase
    def __init__(self, nombre, tiquetes):
        self.nombre = nombre
        self.tiquetes = tiquetes

#Self hace referencia a la instancia que se esta declarando
    def mostrar_invitado(self):
        print('Nombre: {}, Tiquetes: {}'.format(self.nombre, self.tiquetes))

#hace es suma uno a la propiedad tiquetes y muestra un tiquete
    def agregar_tiquete(self):
        print('{} el número de tiquetes ahora es {}'.format(self.nombre, self.tiquetes))

#Se crea la instancia llama a la clase y crea el nombre y los tiquetes de cada persona
invitado1 = Invitado('Fernando', 2)
invitado2 = Invitado('Maria', 4)
invitado1.mostrar_invitado()
invitado2.mostrar_invitado()
invitado2.agregar_tiquete()
invitado2.agregar_tiquete()

