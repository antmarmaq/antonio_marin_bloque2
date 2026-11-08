from colorama import *

from .display import cls, confirm, menu_de_detalles, title
from .operaciones import add_task, input_date


def new_task(tasks):
    cls()
    title()
    # Input de información de la tarea
    name = input("Introduzca el nombre de la tarea: ")
    details = {}
    while True:
        cls()
        title()
        print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
        menu_de_detalles()
        opcion = input("Escriba el número del detalle que quiere añadir: ")
        if opcion == "1":
            cls()
            title()
            print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
            details["description"] = input(
                Fore.YELLOW
                + "Escriba una breve descripción de su tares: "
                + Style.RESET_ALL
            )

        if opcion == "2":
            cls()
            title()
            print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
            while True:
                try:
                    priority = int(
                        input(
                            Fore.YELLOW
                            + "Evalue la prioridad de su tare del 1 al 10: "
                            + Style.RESET_ALL
                        )
                    )
                    if priority not in range(11):
                        details["priority"] = priority
                        continue
                    else:
                        break
                except ValueError:
                    continue

        if opcion == "3":
            cls()
            title()
            print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
            details["deadline"] = input_date()

        if opcion == "4":
            cls()
            title()
            print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
            details["tags"] = (
                input(
                    Fore.YELLOW
                    + "Escriba las etiquetas que le gustaría añadir a la tarea: "
                    + Style.RESET_ALL
                )
                .lower()
                .replace(",", " ")
                .split()
            )

        if opcion == "5":
            cls()
            title()
            name = input(
                Fore.YELLOW + "Escriba el nuevo nombre de la tarea: " + Style.RESET_ALL
            )

        if opcion == "6":
            cls()
            title()
            print(Fore.GREEN + f"Tarea {name} añadida correctamente" + Style.RESET_ALL)
            tasks.append(add_task(name, **details))
            confirm()
            break
    return tasks


def show_list(tasks):
    cls()
    title()
    if not tasks:
        print(Fore.RED + "No hay tareas en la lista" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + Style.BRIGHT + "Lista de tareas:\n" + Style.RESET_ALL)
        for task in tasks:
            print(f"- {task['nombre']}")
        print()
    confirm()


def search_task(tasks):
    pass
