class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor"

objeto = MiClase()
print(objeto._atributo_privado)




'''
class MiClase:
    def __init__(self):
        self.__satributo_privado = "Valor"

    def __hablar(self):
        print("hola, como estass")

objeto = MiClase()
print(objeto.__hablar())
'''