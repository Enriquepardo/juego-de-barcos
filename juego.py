import sys

from clases.Case import *
from clases.Barco import *
from clases.Tablero import *
from clases.Conventions import *
from clases import Tablero

from introducir import (
    solicitar_introducir_numero_extremo,
    solicitar_introducir_si_o_no,
    solicitar_introducir_letra,
    solicitar_introducir_palabra,
    solicitar_introducir_casilla,
)


LONGITUDES_BARCOS = [2, 3, 3, 4, 4, 5]
ORDINAL = 0x2680



def probar_fin_juego(self):
        """Permite probar si el juego ha terminado o no"""
        if len(casillas_ocupadas - self.casillas_jugadas) == 0:
            print("Bravo. El juego ha terminado !")
            return True

        return False


def jugar_tirada(self):
        """Permite gestionar el dato introducido de una tirada"""
        while True:
            nombre_casilla = solicitar_introducir_casilla(
                "Seleccionar una casilla (letra + cifra)")
            # Encontrar la casilla a partir de su nombre
            casilla = instances[nombre_casilla]
            # Probar si la casilla ya ha sido jugada
            if casilla.jugada:
                print("Esta casilla ya ha sido jugada, elija otra",
                    file=sys.stderr)
            else:
                casilla.jugar()
                break

def jugar_una_partida():
    """Algoritmo de una partida"""
    # Creamos un tablero de juego vacío

    tablero = Tablero()

    while True:
        tablero.ver()

        tablero.jugar_tirada()

        if tablero.probar_fin_juego():
            # Si el juego ha terminado, salimos de la función
            tablero.ver()
            return


def elegir_jugarOtra():
    return solicitar_introducir_si_o_no(
        "¿Desea volver a jugar? ? [s/n]")


def jugar():
    while True:
        jugar_una_partida()

        if not elegir_jugarOtra():
            return
