usuarios = {
    "coordinador": "coordinador",
    "camper": "camper",
    "trainer": "trainer"
}

from crud import cargar_todo, guardar_todo, campers, trainer
from messages import menu_coordinador, menu_camper, menu_trainer
import utils as u 

cargar_todo()

def main():
    while True:
        u.clear_screen()
        print("===== SISTEMA CAMPUSLANDS =====")
        print("1. Iniciar como Coordinador")
        print("2. Iniciar como Trainer")
        print("3. Iniciar como Camper")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            menu_coordinador()
        elif opcion == "2":
            id_trainer = input("Ingrese su ID de trainer: ")
            if id_trainer in trainer:
                menu_trainer(id_trainer)
            else:
                print("❌ Trainer no encontrado")
                u.pause()
        elif opcion == "3":
            id_camper = input("Ingrese su ID de camper: ")
            if id_camper in campers:
                menu_camper(id_camper)
            else:
                print("❌ Camper no encontrado")
                u.pause()
        elif opcion == "0":
            print("¡Hasta pronto!")
            guardar_todo()
            break
        else:
            print("❌ Opción inválida")
            u.pause()

if __name__ == "__main__":
    main()

