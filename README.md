# Sistema de Gestión de Campers

## 📌 Descripción del Proyecto

El **Sistema de Gestión de Campers** es una aplicación diseñada para administrar y organizar la información académica y logística de los campers dentro de un entorno de formación tecnológica.

El sistema permite gestionar:

- Registro de campers
- Asignación de salones
- Gestión de cursos y materias
- Administración de trainers
- Organización de horarios y relaciones académicas

El objetivo principal es optimizar la gestión de la información, facilitar el seguimiento académico y mejorar la organización dentro del campus.

---

# 🚀 Funcionalidades Principales

## 👨‍🎓 Gestión de Campers
- Registrar nuevos campers
- Editar información de campers
- Consultar campers registrados
- Eliminar campers

## 🏫 Gestión de Salones
- Crear y administrar salones
- Asignar campers a un salón
- Controlar capacidad de cada salón

## 📚 Gestión de Cursos y Materias
- Crear cursos
- Asignar materias a cada curso
- Relacionar campers con cursos específicos

## 👨‍🏫 Gestión de Trainers
- Registrar trainers
- Asignar trainers a materias
- Consultar información de trainers

## 📊 Organización Académica
- Relación entre campers, cursos y materias
- Visualización estructurada de la información
- Administración centralizada de datos

---

# 🛠️ Tecnologías Utilizadas

- Python
- JSON para almacenamiento de información
- Programación Orientada a Objetos (POO)
- Git y GitHub para control de versiones

---

# 📂 Estructura del Proyecto

```bash
SistemaGestionCampers/
│
├── data/
│   ├── campers.json
│   ├── trainers.json
│   ├── cursos.json
│   ├── materias.json
│   └── salones.json
│
├── modules/
│   ├── campers.py
│   ├── trainers.py
│   ├── cursos.py
│   ├── materias.py
│   └── salones.py
│
├── utils/
│   └── helpers.py
│
├── main.py
└── README.md
```

---

# ⚙️ Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/sistema-gestion-campers.git
```

## 2. Entrar al proyecto

```bash
cd sistema-gestion-campers
```

## 3. Ejecutar el sistema

```bash
python main.py
```

---

# 💾 Almacenamiento de Datos

El sistema utiliza archivos JSON para almacenar la información de manera estructurada.

### Ejemplo:

```json
{
  "id": 1,
  "nombre": "Shirly Leal",
  "curso": "Backend Python",
  "salon": "A1"
}
```

---

# 🧠 Modelo de Relación

El sistema maneja relaciones entre:

- Un camper puede pertenecer a un curso
- Un curso puede tener varias materias
- Un trainer puede impartir varias materias
- Un salón puede contener múltiples campers

---

# 🎯 Objetivos del Proyecto

- Mejorar la organización académica
- Facilitar la gestión de campers y trainers
- Automatizar procesos administrativos
- Aplicar conceptos de programación orientada a objetos
- Implementar almacenamiento estructurado con JSON

---

# 📈 Futuras Mejoras

- Interfaz gráfica
- Base de datos MySQL
- Sistema de autenticación
- Gestión de notas y asistencia
- API REST
- Panel administrativo web

---

# 👩‍💻 Autor

**Shirly Katherinn Leal Nieves**  
Desarrolladora de Software Junior

GitHub: https://github.com/shirlyk89

---

# 📄 Licencia

Este proyecto fue desarrollado con fines educativos y de aprendizaje.
