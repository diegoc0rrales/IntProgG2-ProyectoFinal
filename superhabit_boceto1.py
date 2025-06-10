import random
import datetime
import os

# ════════════════════════════════════════════════════════════════════
# Carga de datos al iniciar el programa (RF-009)
# ════════════════════════════════════════════════════════════════════
habitos = []
cumplimiento = []

if os.path.exists("habitos.txt"):
    with open("habitos.txt", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split("|")
            partes[4] = int(partes[4])
            habitos.append(partes)

if os.path.exists("cumplimiento.txt"):
    with open("cumplimiento.txt", "r") as archivo:
        for linea in archivo:
            porcentajes = linea.strip().split(",")
            cumplimiento.append([int(p) for p in porcentajes if p != ""])
else:
    for _ in range(len(habitos)):
        cumplimiento.append([])

# ════════════════════════════════════════════════════════════════════
# Frases motivadoras (RF-005)
# ════════════════════════════════════════════════════════════════════
mensajes = [
    "¡Sigue así, lo estás haciendo genial!",
    "Cada día cuenta, no te rindas.",
    "Un paso a la vez, ¡vas muy bien!",
    "Constancia es mejor que perfección.",
    "¡Ya estás construyendo tu mejor versión!"
]

# ════════════════════════════════════════════════════════════════════
# Función: Agregar nuevo hábito (RF-001, RF-006, RF-010)
# ════════════════════════════════════════════════════════════════════
def agregar_habito():
    print("\n--- Agregar nuevo hábito ---")
    nombre = input("Nombre del hábito: ")

    while True:
        frecuencia = input("Frecuencia (diaria/semanal): ").lower()
        if frecuencia in ["diaria", "semanal"]:
            break
        else:
            print("⚠️ Ingresa solo 'diaria' o 'semanal'.")

    duracion = input("Duración estimada: ")
    horario = input("Horario sugerido (opcional): ")

    veces = 1
    if frecuencia == "diaria":
        while True:
            veces_input = input("¿Cuántas veces por día?: ")
            if veces_input.isdigit() and int(veces_input) > 0:
                veces = int(veces_input)
                break
            else:
                print("⚠️ Ingresa un número entero mayor que cero.")

    nuevo = [nombre, frecuencia, duracion, horario, veces]
    habitos.append(nuevo)
    cumplimiento.append([])
    print("✅ Hábito agregado correctamente.")

# ════════════════════════════════════════════════════════════════════
# Función: Ver hábitos del día (RF-002)
# ════════════════════════════════════════════════════════════════════
def ver_agenda():
    print("\n📅 Hábitos del día:")
    hoy = datetime.date.today()
    dia_semana = hoy.weekday()
    for i in range(len(habitos)):
        h = habitos[i]
        if h[1] == "diaria" or (h[1] == "semanal" and dia_semana == 0):
            veces = f" x{h[4]}" if h[1] == "diaria" and h[4] > 1 else ""
            print(str(i+1) + ". " + h[0] + veces + " (" + h[2] + ")" +
                  (" - Horario: " + h[3] if h[3] != "" else ""))

# ════════════════════════════════════════════════════════════════════
# Función: Marcar cumplimiento (RF-003, RF-010)
# ════════════════════════════════════════════════════════════════════
def marcar_cumplimiento():
    hoy = datetime.date.today()
    dia_semana = hoy.weekday()
    print("\n✔️ Marca cuántas veces hiciste cada hábito hoy:")
    for i in range(len(habitos)):
        h = habitos[i]
        if h[1] == "diaria":
            while True:
                rep = input(f"¿Cuántas veces hiciste '{h[0]}' hoy? (0-{h[4]}): ")
                if rep.isdigit():
                    r = int(rep)
                    if 0 <= r <= h[4]:
                        porcentaje = int((r / h[4]) * 100)
                        cumplimiento[i].append(porcentaje)
                        break
                print("⚠️ Ingresa un número válido.")
        elif h[1] == "semanal" and dia_semana == 0:
            hecho = input(f"¿Completaste '{h[0]}' hoy? (s/n): ").lower()
            cumplimiento[i].append(100 if hecho == "s" else 0)
    print("\n💬 Mensaje motivacional del día:")
    print(random.choice(mensajes))

# ════════════════════════════════════════════════════════════════════
# Función: Mostrar progreso (RF-004)
# ════════════════════════════════════════════════════════════════════
def ver_progreso():
    print("\n📊 Progreso de la semana:")
    for i in range(len(habitos)):
        h = habitos[i]
        registros = cumplimiento[i]
        if h[1] == "diaria":
            if len(registros) > 0:
                promedio = sum(registros) / len(registros)
            else:
                promedio = 0
            print(h[0] + ": " + str(int(promedio)) + "% promedio diario")
        elif h[1] == "semanal":
            if len(registros) > 0 and registros[-1] == 100:
                print(h[0] + ": completado esta semana ✅")
            else:
                print(h[0] + ": pendiente esta semana ❗")

# ════════════════════════════════════════════════════════════════════
# Función: Guardar datos (RF-008)
# ════════════════════════════════════════════════════════════════════
def guardar_datos():
    with open("habitos.txt", "w") as archivo:
        for h in habitos:
            linea = f"{h[0]}|{h[1]}|{h[2]}|{h[3]}|{h[4]}\n"
            archivo.write(linea)
    with open("cumplimiento.txt", "w") as archivo:
        for c in cumplimiento:
            linea = ",".join(str(p) for p in c) + "\n"
            archivo.write(linea)

# ════════════════════════════════════════════════════════════════════
# Menú Principal (RF-011)
# ════════════════════════════════════════════════════════════════════
while True:
    print("\n══════════════════════════════════════════")
    print("🏆 SUPERHÁBIT - MENÚ PRINCIPAL")
    print("1. Ver hábitos del día")
    print("2. Marcar hábitos completados")
    print("3. Ver progreso")
    print("4. Agregar nuevo hábito")
    print("5. Salir")
    print("══════════════════════════════════════════")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        ver_agenda()
    elif opcion == "2":
        marcar_cumplimiento()
    elif opcion == "3":
        ver_progreso()
    elif opcion == "4":
        agregar_habito()
    elif opcion == "5":
        guardar_datos()
        print("✅ Datos guardados. ¡Hasta pronto!")
        break
    else:
        print("⚠️ Opción inválida. Elige un número del 1 al 5.")
