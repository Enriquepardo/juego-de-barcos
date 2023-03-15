
from clases.Tablero import *
from clases.Case import *
from clases.Conventions import *
from itertools import repeat, product
from random import choice


instances = []
casillas_ocupadas = set()


HORIZONTAL = 0
VERTICAL = 1

ORIENTACIONES = (VERTICAL, HORIZONTAL)

class Barco:
    instances = set()
    def __init__(self, longitud):
            self.longitud = longitud
            self.orientacion = choice(ORIENTACIONES)
            self.tocado = False
            self.hundido = False

            # performance / legibilidad:
            num_lineas = tablero_num_lineas
            num_columnas = tablero_num_columnas
            num2l = generar_num_linea
            num2c = generar_num_columna

            while True:
                if self.orientacion == HORIZONTAL:
                    rang = choice(range(num_lineas))
                    primero = choice(range(num_columnas + 1 - longitud))
                    letra = num2l(rang)
                    cifras = [num2c(x) for x in range(primero, primero + longitud)]
                    self.casillas = {instances[l + c]
                                for l, c in product(repeat(letra, longitud), cifras)}
                else:
                    rang = choice(range(num_columnas))
                    primero = choice(range(num_lineas + 1 - longitud))
                    cifra = num2c(rang)
                    letras = [num2l(x) for x in range(primero, primero + longitud)]
                    # Crear el barco
                    self.casillas = {instances[l + c]
                                for l, c in product(letras, repeat(cifra, longitud))}

                for existente in instances:
                    if self.casillas.intersection(existente.casillas):
                        break  # break relativo al "for existente in barcos:"
                else:
                    # Agregar el barco en el contenedor de barcos
                    instances.append(self)
                    # Informar la casilla que contiene un barco.
                    for casilla in self.casillas:
                        casilla.barco = self
                    # Agregar estas casillas a las casillas ocupadas :
                    casillas_ocupadas |= self.casillas
                    break  # break relativo al "while True:"

    @classmethod
    def generar_barcos(cls):
            for longitud in barcos_longitud:
                Barco(longitud)


