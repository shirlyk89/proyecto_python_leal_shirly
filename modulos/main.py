usuarios = {
    "coordinador": "coordinador",
    "camper": "camper",
    "trainer": "trainer"
}

from crud import guardar_campers, guardar_todo, exportar_trainer, cargar_datos
from messages import menu_coordinador, menu_camper, menu_trainer, examen
import utils as u 

guardar_campers()
cargar_datos('nombre_archivo')
exportar_trainer()

def main():
    while True:
        u.clear_screen()
        print("===== SISTEMA CAMPUSLANDS =====")
        print("1. Iniciar como Coordinador")
        print("2. Iniciar como Trainer")
        print("3. Iniciar como Camper")
        print("4. EXAMEN")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            id_coordinador=input("Ingrese su ID de coordinador: ")
            if id_coordinador == "coordinador":
                menu_coordinador()
        elif opcion == "2":
            id_trainer = input("Ingrese su ID de trainer: ")
            if id_trainer == "trianer":
                menu_trainer(id_trainer)
            else:
                print("❌ Trainer no encontrado")
                u.pause()
        elif opcion == "3":
            id_camper = input("Ingrese su ID de camper: ")
            if id_camper == "camper":
                menu_camper(id_camper)
            else:
                print("❌ Camper no encontrado")
                u.pause()
        elif opcion == "4":
            print("visualizacion rutas asignadas a trainer")
            cargar_datos('nombre_archivo')
            examen()
        elif opcion == "0":
            print("¡Hasta pronto!")
            guardar_todo()
            break
        else:
            print("❌ Opción inválida")
            u.pause()

if __name__ == "__main__":
    main()

