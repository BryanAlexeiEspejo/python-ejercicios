class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

dalto = Persona("Lucas", 22)
print(dalto._edad)
'''

'''
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

dalto = Persona("Lucas", 21)

nombre = dalto.get_nombre()
print(nombre)