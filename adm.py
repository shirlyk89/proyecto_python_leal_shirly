# diccionario de rutas
# Estructura(ruta->modulos->contenido)

rutas:dict[str, dict]={
    "notejs":{
        "nombre": "ruta notejs",
            "modulos":{
                "fundamentos de progrmacion":["algoritmia", "pseint", "python"],
                "progrmacion web":["HTML", "CSS", "Bootstrap"],
                "Bases de datos": {"principal": "MySQL", "alternativo":"MongoBD" },
                "programacion formal":["java", "java script", "C#"],
                "backend":["netcore", "Spring Boot", "NodeJS", "Express"]
    }
},

"Java":{
    "nombre": "ruta Java",
    "modulos":{
        "fundamentos de progrmacion":["algoritmia", "pseint", "python"],
        "progrmacion web":["HTML", "CSS", "Bootstrap"],
        "Bases de datos": {"principal": "MySQL", "alternativo":"MongoBD" },
        "programacion formal":["java", "java script", "C#"],
        "backend":["netcore", "Spring Boot", "NodeJS", "Express"]
        }
    },

    "netcore":{
            "nombre": "ruta netcore",
            "modulos":{
                "fundamentos de progrmacion":["algoritmia", "pseint", "python"],
                "progrmacion web":["HTML", "CSS", "Bootstrap"],
                "Bases de datos": {"principal": "MySQL", "alternativo":"MongoBD" },
                "programacion formal":["java", "java script", "C#"],
                "backend":["netcore", "Spring Boot", "NodeJS", "Express"]
                        }
                        
            }
}

campers:dict[str,dict]={}

def ver_rutas():
    for codigo_ruta, datos_ruta in rutas.items():
        print(f"\n-> codigo: {codigo_ruta}")
        print(f"\n-> nombre: {datos_ruta['nombre']}")
        print(" modulos")
        for modulo, contenido in datos_ruta["modulos"].items():
            print(f"-{modulo}: {contenido}")


#codigo -> clave identificador del diccionario: "notejs", "java", "netcore"
def crear_ruta( nombre:str, modulos:dict):
    codigo=int(input("Ingrese el codigo de la ruta: "))
    if codigo in rutas:
        print("❌ Ya existe esta ruta")
    else: rutas[codigo]={"nombre": nombre, "modulos": modulos}
    print("✅ Ruta creada")

trainer={}

def crear_trainer():
    id_trainer=int(input("Cree el numero de id para el teiner: "))
    if id_trainer in trainer:
        print("❌ Ese trainer ya existe")
        return
    
    nombre=input("Ingrese el nombre del trainer: ")
    apellidos=input("Ingrese los apellidos completos del trainer: ")
    trainer[id_trainer]={
        "id_trainer":id_trainer,
        "nombre":nombre,
        "apellidos":apellidos,
    }
    print(f"✅ El trainer {nombre} {apellidos} ha sido creado con el id: {id_trainer}")

def ver_trainers():
    if not trainer:
        print(" No hay trainers registrados todavía.")
        return

    print("\n📋 LISTA DE TRAINERS")
    for id_trainer, datos in trainer.items():
        print(f"➡ ID: {id_trainer}")
        print(f"   Nombre: {datos['nombre']} {datos['apellidos']}")


def crear_camper():
    id_camper = input("cree el id para este camper: ")
    nombre = input("Ingrese nombre del camper: ")
    apellidos = input("Ingrese apellidos completos: ")
    direccion = input("Direccion: ")
    acudiente = input("Nombre del acudiente: ")
    celular = int(input("Ingrese numero de celular: "))
    tel_fijo = int(input("Ingrese numero fijo: "))

    campers[id_camper] = {
        "nombre": nombre,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "celular": celular,
        "tel_fijo": tel_fijo,
        "ruta": None,
        "programacion_formal": None,    
        "notas": {},            # aquí se irán guardando los módulos y calificaciones
        "estado": "Inscrito"
    }

    print(f"✅ Camper {nombre} {apellidos} creado con ID {id_camper} en estado 'Inscrito'")


def ver_campers():
    print("\n📋 Lista de campers inscritos:")
    if not campers:   # si el diccionario está vacío
        print("⚠️ No hay campers registrados.")
        return
    
    for id_camper, datos in campers.items():
        print(f"   {id_camper} → {datos['nombre']} {datos['apellidos']}")

def asignar_ruta():
    id_camper = input("Ingrese ID del camper: ")
    if id_camper not in campers:
        print("❌ Camper no encontrado.")
        return
    
    ver_rutas()
    codigo = input("Ingrese el código de la ruta a asignar: ")
    if codigo in rutas:
        campers[id_camper]["ruta"] = codigo
        print(f"✅ Ruta {codigo} asignada a {campers[id_camper]['nombre']}")
    else:
        print("❌ Código de ruta inválido.")

def asignar_programacion_formal():
    id_camper = input("Ingrese ID del camper: ")
    if id_camper not in campers:
        print("❌ Camper no encontrado.")
        return
    
    datos = campers[id_camper]
    if not datos["ruta"]:
        print("❌ Este camper no tiene ruta asignada aún.")
        return

    opciones = rutas[datos["ruta"]]["modulos"]["Programación Formal"]
    print(f"\nOpciones de Programación Formal: {opciones}")
    lenguaje = input("Ingrese el lenguaje a asignar: ")

    if lenguaje in opciones:
        datos["programacion_formal"] = lenguaje
        print(f"✅ Asignado {lenguaje} a {datos['nombre']}")
    else:
        print("❌ Lenguaje no válido.")


clase:dict[str,dict]={}

def crear_clase():
    codigo_clase=int(input("Ingrese el codigo de la clase: "))
    ruta=input("Ingrese la ruta: ")
    horario=input("ingrese el horario: ")
    trainer=input("Ingrese el trainer: ")

    if codigo_clase in clase:
        print("❌ Esa clase ya existe")
    else:
        clase[codigo_clase] = {
            "ruta": ruta,
            "horario": horario,
            "trainer": trainer,
            "campers": []
        }
        print(f"✅ Clase {codigo_clase} creada en la ruta {ruta}")

def asignar_clase(): 
    codigo_clase=input("Codigo de la clase: ")
    id_camper=int(input("numero de id camper: "))
    if codigo_clase not in clase:
            print("❌ Esa clase no existe")
            return

    elif id_camper not in campers:
            print("❌ Ese camper no existe")
            return
    
    # Verificar que el camper esté aprobado en sus módulos
    if "notas" not in campers[id_camper]:
        print("❌ Ese camper no tiene notas registradas")
        return

    aprobado = True  # asumimos que está aprobado
    for nota in campers[id_camper]["notas"].values():
        if nota["estado"] != "Aprobado":
            aprobado = False
        break 
    if not aprobado:
        print("❌ Ese camper no está aprobado, no puede asignarse a clases")
        return
    
    ver_campers_aprobados()

    if len(clase[codigo_clase]["campers"]) >= 33:
            print("❌ La clase ya tiene 33 campers")
            return
    
    id_trainer = input("Ingrese el ID del trainer para esta clase: ")

    if id_trainer not in trainer:
        print("❌ Ese trainer no existe")
        return

    # Verificar si el trainer ya tiene clase en el mismo horario
    horario_clase = clase[codigo_clase]["horario"]

    for codigo, datos in clase.items():
        if datos["trainer"] == id_trainer and datos["horario"] == horario_clase:
            print(f"❌ Ese trainer ya tiene otra clase en el mismo horario {codigo}")
            return
        if id_camper in datos["campers"]:
            print(f"❌ El camper {id_camper} ya está en la clase {codigo}")
            return

    # Si no había trainer asignado aún, lo guardamos
    clase[codigo_clase]["trainer"] = id_trainer

    clase[codigo_clase]["campers"].append(id_camper)
    campers[id_camper]["ruta"] = clase[codigo_clase]["ruta"] 
    # se vincula al camper
    print(f"✅ Camper {id_camper} asignado a la clase {codigo_clase} con el trainer: {id_trainer}")

def crear_nota_modulo():
    ver_campers()
    id_camper=input("Ingrese el numero de id del camper: ")
    if id_camper not in campers:
        print("❌ Ese camper no existe")
        return
    ver_rutas()
    modulo=input("Ingrese el nombre del modulo: ")
    
    try:
        quices = float(input("Ingrese la nota de quices/trabajos (0-100): "))
        teorica = float(input("Ingrese la nota de la prueba teórica (0-100): "))
        practica = float(input("Ingrese la nota de la prueba práctica (0-100): "))
    except ValueError:
        print("⚠️ Debe ingresar valores numéricos.")
        return

    # Calcular nota final
    nota_final = (quices * 0.1) + (teorica * 0.3) + (practica * 0.6)
    estado = "Aprobado" if nota_final >= 60 else "Reprobado"

    if nota_final < 60:
        print(f"camper {campers[id_camper]['nombre']} BAJO RENDIMIENTO. llamado de atencion por estar en riesgo ")
        print(f"Nota final: {nota_final:.2f} ❌")
    else:
        print(f"camper {campers[id_camper]['nombre']} Rendimiento aceptable")
        print(f"Nota final: {nota_final:.2f} 😊")

    if "notas" not in campers[id_camper]:
        campers[id_camper]["notas"] = {}

    campers[id_camper]["notas"][modulo] = {
        "quices": quices,
        "teorica": teorica,
        "practica": practica,
        "final": nota_final,
        "estado": estado
    }

    print(f"\n✅ Nota registrada para {campers[id_camper]['nombre']} en {modulo}")
    print(f"   📊 Nota final: {nota_final:.2f} → {estado}")


def ver_campers_aprobados():
    print("\n✅ Lista de campers aprobados:")

    encontrados = False
    for id_camper, datos in campers.items():
        if "notas" in datos:
            # Verificamos si al menos un módulo está aprobado
            for modulo, nota in datos["notas"].items():
                if nota["estado"] == "Aprobado":
                    print(f" - {id_camper}: {datos['nombre']} {datos['apellidos']} | Módulo: {modulo} | Nota final: {nota['final']}")
                    encontrados = True
    if not encontrados:
        print("⚠️ No hay campers aprobados aún.")


def reportar_inscritos():
    print("📋 Campers en estado INSCRITO:")
    for id_c, datos in campers.items():
        if datos.get("estado") == "Inscrito":
            print(f"ID: {id_c} - {datos['nombre']}")

def reportar_aprobados_inicial():
    print("✅ Campers que aprobaron el examen inicial:")
    for id_c, datos in campers.items():
        if datos.get("estado") == "Aprobado":
            print(f"ID: {id_c} - {datos['nombre']}")

def reportar_trainers():
    print(" Entrenadores en CampusLands:")
    for id_t, datos in trainer.items():
        print(f"ID: {id_t} - {datos['nombre']} {datos['apellidos']}")

def reportar_bajo_rendimiento():
    print("⚠️ Campers con BAJO RENDIMIENTO:")
    encontrados=False
    for id_c, datos in campers.items():
        notas = datos.get("notas", {})
        for modulo, info in notas.items():
            if info["final"] < 60:
                print(f"ID: {id_c} - {datos['nombre']} - Módulo: {modulo} - Nota: {info['final']}")
                encontrados=True
    if not encontrados:
        print("✔ No hay campers con bajo rendimiento.")


def reportar_asociados_ruta():
    print("📚 Campers y Trainers asociados a rutas:")
    for cod_clase, datos in clase.items():
        ruta = datos["ruta"]
        trainer_id = datos["trainer"]
        trainer_nombre = trainer[trainer_id]["nombre"] if trainer_id in trainer else "No asignado"

        print(f"\nClase: {cod_clase} | Ruta: {ruta} | Trainer: {trainer_nombre}")
        for id_c in datos["campers"]:
            print(f"  --> Camper: {id_c} - {campers[id_c]['nombre']}")


def reportar_resultados_modulos():
    print("📊 Resultados por Ruta, Trainer y Módulos:")
    for cod_clase, datos in clase.items():
        ruta = datos["ruta"]
        trainer_id = datos["trainer"]
        trainer_nombre = trainer[trainer_id]["nombre"] if trainer_id in trainer else "No asignado"

        print(f"\nClase: {cod_clase} | Ruta: {ruta} | Trainer: {trainer_nombre}")
        
        conteo = {}  # {modulo: {"aprobados": x, "reprobados": y}}

        for id_c in datos["campers"]:
            notas = campers[id_c].get("notas", {})
            for modulo, info in notas.items():
                if modulo not in conteo:
                    conteo[modulo] = {"aprobados": 0, "reprobados": 0}
                if info["estado"] == "Aprobado":
                    conteo[modulo]["aprobados"] += 1
                else:
                    conteo[modulo]["reprobados"] += 1

        # Mostrar resultados
        for modulo, valores in conteo.items():
            print(f"  --> Módulo: {modulo} → Aprobados: {valores['aprobados']} | Reprobados: {valores['reprobados']}")


def ver_bases_datos():
    id_camper = input("Ingrese ID del camper: ")
    if id_camper not in campers:
        print("❌ Camper no encontrado.")
        return

    datos = campers[id_camper]
    if not datos["ruta"]:
        print("❌ Este camper no tiene ruta asignada aún.")
        return

    bd = rutas[datos["ruta"]]["modulos"]["Bases de datos"]
    print(f"\n Camper: {datos['nombre']}")
    print(f"   Ruta: {datos['ruta']}")
    print(f"   Base de datos principal: {bd['principal']}")
    print(f"   Base de datos alternativo: {bd['alternativo']}")

