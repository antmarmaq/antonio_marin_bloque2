from app.display import cls, confirm, menu, title
from app.modelos import new_task, show_list
from app.operaciones import add_task

"""
// 1. INICIALIZACIÓN
MIENTRAS Verdadero:
    MOSTRAR Titulo
    MOSTRAR Menu
    accion = PEDIR Selecionar (1,2,3)

    // 2. Procesar la selección
    SI accion == "1":
        PEDIR nombre de la tarea
        PEDIR 

"""
while True:
    cls()
    title()
    menu()
    action = input("Seleccione lo que quiere hacer (1, 2 o 3)")

    if action == "1":
        print("adding task")
        new_task()
        confirm()
    if action == "2":
        print("showing list")
        show_list()
        confirm()
    if action == "3":
        break
    else:
        continue
