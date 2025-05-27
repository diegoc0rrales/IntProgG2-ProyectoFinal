import random
import datetime

# Lista para guardar los hábitos
habitos = []       # Cada hábito: [nombre, frecuencia, duración, horario, veces_por_dia]
cumplimiento = []  # Para cada hábito, se guarda una lista con los registros diarios (en %)

# Frases motivadoras
mensajes = [
    "¡Sigue así, lo estás haciendo genial!",
    "Cada día cuenta, no te rindas.",
    "Un paso a la vez, ¡vas muy bien!",
    "Constancia es mejor que perfección.",
    "¡Ya estás construyendo tu mejor versión!"
]

# Paso 1: Registrar hábitos
print("Bienvenido a SuperHábit - Tu entrenador de hábitos 💪\n")

while True:
    print("--- Agrega un nuevo hábito ---")
    nombre = input("Nombre del hábito: ")
    frecuencia = input("Frecuencia (diaria/semanal): ").lower()
    duracion = input("Duración estimada (ej: 30 minutos, 2 semanas): ")
    horario = input("Horario sugerido (opcional, presiona Enter si no tienes): ")

    veces_por_dia = 1
    if frecuencia == "diaria":
        veces_input = input("¿Cuántas veces deseas realizar este hábito por día?: ")
        if veces_input.isdigit():
            veces_por_dia = int(veces_input)

    nuevo_habito = [nombre, frecuencia, duracion, horario, veces_por_dia]
    habitos.append(nuevo_habito)
    cumplimiento.append([])

    otra = input("¿Quieres agregar otro hábito? (s/n): ").lower()
    if otra != "s":
        break

# Paso 2: Mostrar hábitos del día
print("\n📅 Hábitos del día:")
hoy = datetime.date.today()
dia_semana = hoy.weekday()  # lunes = 0

for i in range(len(habitos)):
    h = habitos[i]
    if h[1] == "diaria" or (h[1] == "semanal" and dia_semana == 0):
        veces = f" x{h[4]} veces" if h[1] == "diaria" and h[4] > 1 else ""
        print(str(i+1) + ". " + h[0] + veces + " (" + h[2] + ")" +
              (" - Horario: " + h[3] if h[3] != "" else ""))

# Paso 3: Marcar cumplimiento
print("\n✔️ Marca cuántas veces hiciste cada hábito hoy:")

for i in range(len(habitos)):
    h = habitos[i]
    if h[1] == "diaria":
        veces_hechas = input("¿Cuántas veces hiciste '" + h[0] + "' hoy? (0-" + str(h[4]) + "): ")
        if veces_hechas.isdigit():
            hechas = int(veces_hechas)
            if hechas > h[4]:
                hechas = h[4]  # No más que el máximo
            porcentaje = int((hechas / h[4]) * 100)
            cumplimiento[i].append(porcentaje)
        else:
            cumplimiento[i].append(0)
    elif h[1] == "semanal" and dia_semana == 0:
        hecho = input("¿Completaste '" + h[0] + "' hoy? (s/n): ").lower()
        if hecho == "s":
            cumplimiento[i].append(100)
        else:
            cumplimiento[i].append(0)

# Paso 4: Mostrar progreso
print("\n📊 Progreso esta semana:")

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

# Paso 5: Mensaje motivacional
print("\n💬 Mensaje motivacional del día:")
print(random.choice(mensajes))
