from app.display import cls, menu_ficheros, title
from app.modelos import del_dir, new_dir, new_flat_file, new_binary_file

# Inicializamos creando la lista vacía de tareas.

try:
    while True:
        cls()
        title()
        menu_ficheros()
        action = input("Seleccione el número de la operación a realizar: ")

        if action == "1":
            new_dir()

        if action == "2":
            del_dir()

        if action == "3":
            new_flat_file()

        if action == "4":
            new_binary_file()

        if action == "5":
            continue

        if action == "5":
            continue

        if action == "6":
            continue

        if action == "7":
            break

        else:
            continue

except KeyboardInterrupt:
    print("\nCerrando el programa...")
