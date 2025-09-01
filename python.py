# -*- coding: utf-8 -*-
# CLASES Y OBJETOS
'''
class auto():
    marca = "toshi"
    modelo = "K1299"
    motor = "gama alta"
    
    marca2 = "shi"
    modelo2 = "99987"
    motor2 = "gama media"

auto1 = auto()
auto2 = auto()
auto3 = auto()
auto4 = auto()

print(auto1.marca)
print(auto1.marca2)
'''



# -*- coding: utf-8 -*-
# ATRIBUTOS, METODOS
'''
class Casa:
    def __init__(self, muebles, cocina, deposito):
        self.muebles = muebles
        self.cocina = cocina
        self.deposito = deposito
        
    def llama(self):
        print(f'La llama que llama: {self.muebles}')
        
    def cortar(self):
        print(f'La casa tiene: {self.muebles}')

casa1 = Casa("mesa", "gas", "pequeño")
casa2 = Casa("vitrina", "lavaplatos", "grande")

casa2.llama()
'''



# -*- coding: utf-8 -*-

# EJERCICIO 1 
'''
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")

nombre = input("Dígame su nombre: ")
edad = input("Dígame su edad: ")
grado = input("Dígame su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
DATOS DEL ESTUDIANTE: \n\n
Nombre: {estudiante.nombre} \n
Edad: {estudiante.edad} \n
Grado: {estudiante.grado} \n
""")

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
'''



# HERENCIA
'''
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

roberto = Empleado("Roberto", 43, "argentino", "Programador", 100000)

roberto.hablar()
'''
#HERENCIA MULTIPLE
'''
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f'Hola, soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')

roberto = Artista("Cantar")

# Validaciones
herencia = issubclass(EmpleadoArtista, Persona)
instancia = isinstance(roberto, Artista)   #EmpleadoArtista

print(instancia)
'''

#MRO 
'''
class A:
    def hablar(self):
        print("Hola desde A")

class F:
    def hablar(self):
        print("Hola desde F")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(F):
    def hablar(self):
        print("Hola desde C")

class D(B, C):
    def hablar(self):
        print("Hola desde D")

d = D()

F.hablar(d)
'''


# EJERCICIO 2
'''
class Animal:
    def comer(self):
        print("El animal está comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal está volando")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando")

class Murcielago(Mamifero, Ave):
    pass

ave = Ave()

ave.comer()
ave.volar()

print(Murcielago.__mro__)
'''

#POLIMORFISMO
#1
'''
class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"

gato = Gato()
perro = Perro()

print(perro.sonido())
'''

#2
'''
def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")

lista = [1, 2, 3, 4]
lista2 = "maquina"

recorrer(lista)
'''


#ENCAPSULAMIENTO
#1
'''
class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor"

objeto = MiClase()
print(objeto._atributo_privado)
'''



'''
class MiClase:
    def __init__(self):
        self.__satributo_privado = "Valor"

    def __hablar(self):
        print("hola, como estass")

objeto = MiClase()
print(objeto.__hablar())
'''


# SETTERS Y GETTERS
#1
'''
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
'''

#DECORADORES
#1
'''
def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    return funcion_modificada

def saludo():
    print("Hola Dalto como andas")

saludo_modificado = decorador(saludo)
saludo_modificado()
'''


#DECORADOR PROPERTY
'''
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

dalto = Persona("Lucas", 21)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "Pepe"

nombre = dalto.nombre
print(nombre)

del dalto.nombre

print("que haces maquinola, suscribite")
'''

#ABSTRACCION

'''
class Auto():
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"
        print("El auto está encendido")

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.conducir()
'''


# CLASES ABSTRACTAS
'''
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")

pedrito = Estudiante("Pedrito", 25, "No Binario", "programación")
dalto = Trabajador("Lucas", 21, "Masculino", "programación")

dalto.presentarse()
dalto.hacer_actividad()

pedrito.presentarse()
pedrito.hacer_actividad()
'''


#METODOS ESPECIALES  O DUNDER
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona(nombre={self.nombre},edad={self.edad})'

    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'

    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)


dalto = Persona("Lucas", 21)
pedro = Persona("Pedro", 30)
maria = Persona("Maria", 18)

nueva_persona = dalto + maria
print(nueva_persona.edad)
'''

# EJERCICIO 3 
'''
class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"

    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)


goku = Personaje("Goku", 100, 100)
vegeta = Personaje("Vegeta", 99, 99)
jiren = Personaje("Jiren", 130, 140)

gogeta = goku + vegeta
jireta = gogeta + jiren

print(jireta)
print(gogeta)
print(goku)
print(vegeta)
print(jiren)
'''


#SRP
'''
class TanqueDeCombustible:
    def __init__(self):
        self.combustilbe = 100

    def agregar_combustible(self, cantidad):
        self.combustilbe += cantidad

    def obtener_combustible(self):
        return self.combustilbe

    def usar_combustible(self, cantidad):
        self.combustilbe -= cantidad


class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        return self.posicion


tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtener_posicion())
autito.mover(10)
print(autito.obtener_posicion())
autito.mover(20)
print(autito.obtener_posicion())
autito.mover(60)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())
'''

#OCP
'''
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError


class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")


class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")


class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print(f"Enviando Whatsapp a {self.usuario.whatsapp}")


class NotificadorTwitter(Notificador):
    def Notificar(self):
        print(f"Enviando twit a {self.usuario.twitter}")
'''


#LSC
#1
'''
class Ave:
    def volar(self):
        return "Estoy volando"

class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"

def hacer_volar(ave = Ave):
    return ave.volar()

print(hacer_volar(Pinguino()))
'''


#2
'''
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy Volando"

class AveNoVoladora(Ave):
    pass
'''

# ISP
'''
from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass


class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")


robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()
humano.comer()
'''


#DIP
#1

'''
class Diccionario:
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras
        pass

class CorrectorOrtografico:
    def __init__(self):
        self.diccionario = Diccionario()

    def corregir_texto(self, texto):
        # usamos el diccionario para corregir el texto
        pass
'''

#2
'''
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras si está en el diccionario
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        # usamos el verificador para corregir texto
        pass

corrector = CorrectorOrtografico(ServicioWeb())
'''


# EJERCICIO FINAL


#1
'''
from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negativo"

analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento("this is funny, but is not my interesting")
print(resultado)
'''

#2
import openai

openai.api_key = ""

from openai import OpenAI

client = OpenAI(api_key=openai.api_key)

system_rol = '''
Hace de cuenta que sos un analizador de sentimientos.
Yo te paso sentimientos y vos analizas el sentimiento de los mensajes
y me das una respuesta con al menos 1 caracter y como máximo 4 caracteres
SOLO RESPUESTAS NUMÉRICAS. donde -1 es negatividad máxima, 0 es neutral y 1 es positividad máxima.
(Podés responder solo con ints o floats)
'''

mensajes = [{"role": "system", "content": system_rol}]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.6 and polaridad <= 0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m"
        elif polaridad > -0.3 and polaridad < 0.1:
            return "\x1b[1;31m" + "Algo negativo" + "\x1b[0;37m"
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo" + "\x1b[0;37m"
        elif polaridad >= 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy positivo" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "MUY Negativo" + "\x1b[0;37m"

analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\nDecime Algo: " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=mensajes,
        max_tokens=8
    )

    respuesta = completion.choices[0].message.content
    mensajes.append({"role": "assistant", "content": respuesta})

    try:
        polaridad = float(respuesta)
    except:
        polaridad = 0

    sentimiento = analizador.analizar_sentimiento(polaridad)
    print(sentimiento)
