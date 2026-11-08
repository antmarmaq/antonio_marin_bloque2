from colorama import *


def add_task(nombre, **kwargs):
    """
    Función que usaremospara añadir tareas anuestro programa.
    """
    return {"nombre": nombre, **kwargs}


def input_date():
    """
    Muestra una serie de inputs para dia, mes y año y devuelve una fecha en formato string DD/MM/AAAA
    """
    # Pedimos el día
    while True:
        day = input(Fore.YELLOW + "Escriba el día: " + Style.RESET_ALL)
        if len(day) <= 2:
            try:
                if 0 < int(day) < 32:
                    if len(day) == 1:
                        month = "0" + day
                    break
                else:
                    continue
            except ValueError:
                continue
        else:
            continue
    # Pedimos el mes
    while True:
        month = input(Fore.YELLOW + "Escriba el mes: " + Style.RESET_ALL)
        if len(month) <= 2:
            try:
                if 0 < int(month) < 13:
                    break
                if len(month) == 1:
                    month = "0" + month
                else:
                    continue
            except ValueError:
                continue

        else:
            continue
    # Pedimos el año
    while True:
        year = input(Fore.YELLOW + "Escriba el año: " + Style.RESET_ALL)
        if len(year) == 4:
            try:
                if 2026 <= int(year):
                    break
                else:
                    continue
            except ValueError:
                continue
        else:
            continue
    return f"{day}/{month}/{year}"
