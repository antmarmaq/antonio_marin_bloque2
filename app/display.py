import os

from art import *
from colorama import *


def cls():
    """
    Limpia la pantalla
    """
    os.system("cls" if os.name == "nt" else "clear")


def title():
    """
    Imprime el título de la aplicación
    """
    print(
        Fore.BLUE,
        Style.BRIGHT + text2art("Gestor de Tareas") + Style.RESET_ALL,
    )


def menu():
    """
    Imprime el menu de la aplicación
    """
    print("\U00002554" + 28 * "\U00002550" + "\U00002557")
    print("\U00002551" + " 1. Añadir tarea         \U00002795 " + "\U00002551")
    print("\U00002551" + " 2. Ver lista de tareas  \U0001f4cb " + "\U00002551")
    print("\U00002551" + " 3. Buscar tarea         \U0001f50d " + "\U00002551")
    print("\U00002551" + " 4. Salir del programa   \U0001f44b " + "\U00002551")
    print("\U0000255a" + 28 * "\U00002550" + "\U0000255d\n")


def confirm():
    input("Presione Enter para continuar...")
