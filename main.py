from app.display import cls, confirm, menu, title
from app.modelos import new_task, show_list
from app.operaciones import add_task

"""
// 1. INICIALIZACIÓN
MIENTRAS Verdadero:
    MOSTRAR Titulo
    MOSTRAR Menu
    accion = PEDIR Selecione (1,2,3)

    // 2. Procesar la selección
    SI accion == "1":
        PEDIR nombre de la tarea
        //2.1 Bucle para la opcion uno
        MIENTRAS VERDADERO:
            MOSTRAR Desea añadir detalles a la tarea?
            MOSTRAR 1. Descripción
            MOSTRAR 2. Prioridad
            MOSTRAR 3. Fecha límite
            MOSTRAR 4. Etiqueta
            MOSTRAR 5. Terminar
            opcion = PEDIR Seleccione 1,2,3,4 o 5
            
            SI opcion == "1" ENTONCES
                PEDIR Escriba una descripción de su tarea
                ASIGNAR la descripción dentro de la tarea
            
            SI opcion == "2" ENTONCES
                PEDIR Evalue la prioridad de su tarea del 1 al 10
                ASIGNAR la prioridad a la tarea
            
            SI opcion == "3"ENTONCES
                PEDIR Escriba la fecha limite de su tarea (DD/MM/AAAA)
                ASIGNAR Fecha limite a la tarea
            
            SI opcion == "4" ENTONCES
                etiquetas PEDIR Escriba etiquetas que quiere asignar a su tarea
                PARA etiqueta EN etiquetas
                    ASIGNAR etiqueta a la lista de etiquetas de la tarea
            
            SI opcion == "5" ENTONCES
                END
    
    SI accion == "2" ENTONCES
        MOSTRAR Lista de tareas

    SI accion == "3" ENTONCES
        PEDIR Nombre de la tarea que desea consultar
        MOSTRAR detalles de la tarea
    
    SI accion == "4" ENTONCES
        END
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
