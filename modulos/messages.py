from crud import (
    crear_camper, ver_campers, crear_trainer, ver_trainers, crear_ruta,
    ver_rutas, asignar_ruta, asignar_programacion_formal,
    crear_clase, asignar_clase, crear_nota_modulo,
    ver_campers_aprobados, reportar_inscritos,
    reportar_aprobados_inicial, reportar_trainers,
    reportar_bajo_rendimiento, reportar_asociados_ruta,
    reportar_resultados_modulos, ver_bases_datos
)

from crud import campers, trainer, clase, rutas
import utils as u

def menu_coordinador():
    while True:
        u.clear_screen()
        print("\n===== MENÚ COORDINADOR =====")
        print("1. Crear camper")
        print("2. Ver campers")
        print("3. Crear trainer")
        print("4. Ver trainers")
        print("5. crear ruta")
        print("6. ver rutas")
        print("7. asignar ruta")
        print("8. asignar programacion fromal")
        print("9. crear clase")
        print("10. asignar clase")
        print("11. crear nota modulo")
        print("12. ver campers aprobados")
        print("13. reportar inscritos")
        print("14. reportar aprobados inicial")
        print("15. reportar trainers")
        print("16. reportar bajo rendimiento")
        print("17. reportar asociados a ruta")
        print("18. reportar resultados modulo")
        print("19. ver bases de datos")
        print("0. Cerrar sesión")
        opcion = input("Opción: ")

        if opcion == "1":
            u.clear_screen()
            crear_camper()
            u.pause()
        elif opcion == "2":
            u.clear_screen()
            ver_campers()
            u.pause()
        elif opcion == "3":
            u.clear_screen()
            crear_trainer()
            u.pause()
        elif opcion == "4":
            u.clear_screen()
            ver_trainers()
            u.pause()
        elif opcion == "5":
            u.clear_screen()
            ver_rutas()
            nombre = input("Ingrese el nombre de la ruta: ")
            modulos = { "fundamentos de programacion": [],
        "programacion web": [],
        "Bases de datos": {"principal": "MySQL", "alternativo": "MongoDB"},
        "programacion formal": [],
        "backend": [] }
            crear_ruta(nombre, modulos) 
            u.pause()
        elif opcion == "6":
            u.clear_screen()
            ver_rutas()
            u.pause()
        elif opcion == "7":
            u.clear_screen()
            asignar_ruta()
            u.pause()
        elif opcion == "8":
            u.clear_screen()
            asignar_programacion_formal()
            u.pause()
        elif opcion == "9":
            u.clear_screen()
            crear_clase()
            u.pause()
        elif opcion == "10":
            u.clear_screen()
            asignar_clase()
            u.pause()
        elif opcion == "11":
            u.clear_screen()
            crear_nota_modulo()
            u.pause()
        elif opcion == "12":
            u.clear_screen()
            ver_campers_aprobados()
        elif opcion == "13":
            u.clear_screen()
            reportar_inscritos()
            u.pause()
        elif opcion == "14":
            u.clear_screen()
            reportar_aprobados_inicial()
            u.pause()
        elif opcion == "15":
            u.clear_screen()
            reportar_trainers()
            u.pause()
        elif opcion == "16":
            u.clear_screen()
            reportar_bajo_rendimiento()
            u.pause()
        elif opcion == "17":
            u.clear_screen()
            reportar_asociados_ruta()
            u.pause()
        elif opcion == "18":
            u.clear_screen()
            reportar_resultados_modulos()
            u.pause()
        elif opcion == "19":
            u.clear_screen()
            ver_bases_datos()
            u.pause()
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida")
            u.pause()

def menu_camper(id_camper):
    while True:
        u.clear_screen()
        print(f"\n===== MENÚ CAMPER ({id_camper}) =====")
        print("1. Ver mis datos")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            datos = campers[id_camper]
            print(f"Nombre: {datos['nombre']} {datos['apellidos']}")
            print(f"Estado: {datos['estado']}")
            print(f"Ruta asignada: {datos['ruta']}")
            u.pause()
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida")
            u.pause()

def menu_trainer(id_trainer):
    while True:
        u.clear_screen()
        print(f"\n===== MENÚ TRAINER ({id_trainer}) =====")
        print("1. Ver campers en mis clases")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            for cod, datos in clase.items():
                if datos["trainer"] == id_trainer:
                    print(f"Clase {cod} - Ruta: {datos['ruta']} - Campers: {datos['campers']}")
            u.pause()
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida")
            u.pause()