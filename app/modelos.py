from colorama import *
from pathlib import Path
import pickle

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
        print(Fore.GREEN + "Añadiendo tarea: " + Style.RESET_ALL + f"{name}")
        menu_de_detalles()
        opcion = input("Escriba el número del detalle que quiere añadir: ")
        if opcion == "1":
            cls()
            title()
            print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
            details["descripcionion"] = input(
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
                        continue
                    else:
                        details["prioridad"] = priority
                        break
                except ValueError:
                    continue

        if opcion == "3":
            cls()
            title()
            print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
            details["fecha limite"] = input_date()

        if opcion == "4":
            cls()
            title()
            print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
            details["etiquetas"] = (
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
        print(Fore.RED + "No hay ninguna tarea en la lista" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + Style.BRIGHT + "Lista de tareas:\n" + Style.RESET_ALL)
        for task in tasks:
            print(f"- {task['nombre']}")
        print()
    confirm()


def search_task(tasks):
    cls()
    title()
    if not tasks:
        print(Fore.RED + "No hay ninguna tarea en la lista" + Style.RESET_ALL)
        confirm()
        return
    else:
        search = input("Escriba la tarea de la que quiere los detalles: ")
        results = []
        for task in tasks:
            if search.lower() in task["nombre"].lower():
                results.append(task)
        if results == []:
            print(
                Fore.RED
                + f"No se ha encontrado ninguna tarea con nombre: {search}"
                + Style.RESET_ALL
            )
            confirm()
        else:
            cls()
            title()
            print(
                Fore.YELLOW
                + Style.BRIGHT
                + f"Se han encontrado {len(results)} resultados para: {search}"
                + Style.RESET_ALL
            )
            index = 1
            for task in results:
                if search.lower() in task["nombre"].lower():
                    print(Fore.YELLOW + f"\nResultado {index}:")
                    index += 1
                    for key, value in task.items():
                        print(Fore.GREEN + f"{key}:" + Style.RESET_ALL + f" {value}")
            print(Style.RESET_ALL)
            confirm()


def new_dir():
    """"
    Pide un nombre y crea un directorio con dicho nombre
    """
    print(Fore.GREEN + "Creando nueva carpeta" + Style.RESET_ALL)
    name = input("Escriba el nombre del directorio a crear: ")
    directory = Path(name)
    directory.mkdir(exist_ok=True)
    print(Fore.GREEN + "Carpeta creada exitosamente." + Style.RESET_ALL)
    confirm()


def del_dir():
    """"
    Pide un nombre y borra un directorio con dicho nombre
    """
    print(Fore.GREEN + "Borrando carpeta" + Style.RESET_ALL)
    name = input("Escriba el nombre del directorio a borrar: ")
    directory = Path(name)
    if directory.exists():
        directory.rmdir()
        print(Fore.GREEN + "Carpeta borrada exitosamente." + Style.RESET_ALL)
    else:
        print(Fore.RED + "No se ha encontrado ninguna carpeta con ese nombre: " + Style.RESET_ALL)
    confirm()


def new_flat_file():
    """
    Pide una carpeta y un nombre de archivo para crear un archivo de texto plano, luego pide que escribas lo que quieres que tenga el archivo y lo crea
    """
    dir_name = input("Escriba el nombre del directorio en el que quiere crear el archivo: ")
    directory = Path(dir_name)
    if directory.exists():
        file_name = input("Escriba el nombre del archivo que quiere crear: ")
        file = directory / f"{file_name}.txt"
        content = input("Escriba el texto que quiere que incluya el archivo:\n")
        file.write_text(content, encoding='utf-8')
        print(Fore.GREEN + "Archivo creado correctamente." + Style.RESET_ALL)
    else:
        print(Fore.RED + "No se ha encontrado ninguna carpeta con ese nombre" + Style.RESET_ALL)
    confirm()


def new_binary_file():
    """
    Pide una carpeta y un nombre de archivo para crear un archivo de texto plano, luego pide que escribas lo que quieres que tenga el archivo y lo crea
    """
    dir_name = input("Escriba el nombre del directorio en el que quiere crear el archivo: ")
    directory = Path(dir_name)
    if directory.exists():
        file_name = input("Escriba el nombre del archivo que quiere crear: ")
        file = directory / f"{file_name}.pkl"
        content = input("Escriba el texto que quiere que incluya el archivo:\n")
        ruta = Path("C:/Users/PYTHON/Desktop/Antonio Marín Maqueda/antonio_marin_bloque2/{dir_name}/{file_name}.pkl")
        with open(f"{file_name}.pkl", 'wb') as f:
            pickle.dump(content,f)
        print(Fore.GREEN + "Archivo creado correctamente." + Style.RESET_ALL)
    else:
        print(Fore.RED + "No se ha encontrado ninguna carpeta con ese nombre" + Style.RESET_ALL)
    confirm()


def del_file():
    pass