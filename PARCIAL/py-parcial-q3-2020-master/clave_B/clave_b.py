import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""


# start-->
def suma(numero1, numero2, numero3):
    suma = numero1 + numero2 + numero3
    return suma


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""


# start-->
def sumaImpares():
    i = 0 
    suma = 0
    while i < 1000:
        i += 1
        if i % 2 != 0:
            suma += i
    result = suma
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m

perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""


# start-->
def definicionEsfera():
    perimetro = obtenerPerimetro()
    area = obtenerArea()
    volumen = obtenerVolumen()
    result = {"perimetro": perimetro, "area": area, "volumen": volumen}
    return result


def obtenerPerimetro():
    perimetro = 2*math.pi*12
    result = perimetro
    return result


def obtenerArea():
    area = 4*math.pi*12*12
    result = area
    return result


def obtenerVolumen():
    volumen = (4/3)*math.pi*12*12*12
    result = volumen
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Esfera:
    def __init__(self):
        self.definicionEsfera = [obtenerPerimetro, obtenerArea, obtenerVolumen]

    def definicionEsfera(self):
        return self.definicionEsfera


"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto
"""


class Banco:
    def __init__(self):
        self.ClienteBD = []

    def banco(self, Cliente):
        self.Cliente = (self, nombre, ciudad, cantidadBonos, tipo, cantMonetaria)

    def procesar(self):
        return 0

    def abonosSanSalvador(self):
        return 0

    def abonosBalYRod(self):
        return 0


class Cliente:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl(url):
    url = "https://github.com/angelarc20/Parcial.git"
    return url
