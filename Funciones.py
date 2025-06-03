def agregar_a_lista(lista, elemento):
    nueva_lista = [0] * (len(lista) + 1)
    for i in range(len(lista)):
        nueva_lista[i] = lista[i]
    nueva_lista[len(lista)] = elemento
    return nueva_lista

def Cargar_participantes(): #1
    participantes = []
    while len(participantes) < 5:
        nombre = input("Ingrese el nombre del participante (mínimo 3 caracteres, solo letras y espacios): ")
        if len(nombre) < 3:
            print("Nombre inválido. Debe tener al menos 3 caracteres.")
            continue
        valido = True
        for c in nombre:
            if not (('a' <= c <= 'z') or ('A' <= c <= 'Z') or c == ' '):
                valido = False
                break
        if not valido:
            print("Nombre inválido. Solo se permiten letras y espacios.")
            continue
        participantes = agregar_a_lista(participantes, nombre)
    return participantes

if __name__ == "__main__":
    participantes = Cargar_participantes()
    print("Participantes cargados:", participantes)

def Cargar_puntuaciones(): #2
    while True:
        try: 
            puntuacion1 = int(input("Ingrese la puntuación del jurado 1 (entre 1 y 10): "))
            if puntuacion1 < 1 or puntuacion1 > 10:
                raise ValueError("Puntuación inválida. Debe estar entre 1 y 10.")
            puntuacion2 = int(input("Ingrese la puntuación del jurado 2 (entre 1 y 10): "))
            if puntuacion2 < 1 or puntuacion2 > 10:
                raise ValueError("Puntuación inválida. Debe estar entre 1 y 10.")
            puntuacion3 = int(input("Ingrese la puntuación del jurado 3 (entre 1 y 10): "))
            if puntuacion3 < 1 or puntuacion3 > 10:
                raise ValueError("Puntuación inválida. Debe estar entre 1 y 10.")
            puntuacion = []
            puntuacion = agregar_a_lista(puntuacion, puntuacion1)
            puntuacion = agregar_a_lista(puntuacion, puntuacion2)
            puntuacion = agregar_a_lista(puntuacion, puntuacion3)
            return puntuacion
        except ValueError as e:
            print("Error:", e)
            print("Por favor, intentá de nuevo.\n")

def Mostrar_puntuaciones(participantes, puntuaciones): #3
    print("Resultados de los participantes:\n")
    for i in range(len(participantes)):
        puntajes = puntuaciones[i]
        total = 0
        for j in range(len(puntajes)):
            total = total + puntajes[j]
        promedio = total / len(puntajes)
        print(f"Participante: {participantes[i]}")
        print(f"  Puntuación Jurado 1: {puntajes[0]}")
        print(f"  Puntuación Jurado 2: {puntajes[1]}")
        print(f"  Puntuación Jurado 3: {puntajes[2]}")
        print(f"  Promedio general: {promedio}")
        print("-" * 30)

def Participantes_con_promedio_mayor_a_4(participantes, puntuaciones): #4
    encontrados = False
    for i in range(len(participantes)):
        total = 0
        for j in range(len(puntuaciones[i])):
            total = total + puntuaciones[i][j]
        cantidad = len(puntuaciones[i])
        promedio = total / cantidad
        if promedio > 4:
            print(participantes[i], "tiene promedio mayor a 4:", promedio)
            encontrados = True
    if not encontrados:
        print("Ningún participante tiene un promedio mayor a 4.")

def Participantes_con_puntuacion_mayor_a_7(participantes, puntuaciones): #5
    encontrados = False
    for i in range(len(participantes)):
        total = 0
        for j in range(len(puntuaciones[i])):
            total = total + puntuaciones[i][j]
        cantidad = len(puntuaciones[i])
        promedio = total / cantidad
        if promedio > 7:
            print(participantes[i], "tiene promedio mayor a 7:", promedio)
            encontrados = True
    if not encontrados:
        print("Ningún participante tiene un promedio mayor a 7.")

def Promedio_de_cada_jurado(puntuaciones): #6
    for i in range(len(puntuaciones[0])):
        total = 0
        for j in range(len(puntuaciones)):
            total = total + puntuaciones[j][i]
        promedio = total / len(puntuaciones)
        print(f"Promedio del jurado {i+1}: {promedio}")

def Jurado_mas_estricto(puntuaciones): #7
    min_promedio = 9999999
    jurado_estricto = -1
    for i in range(len(puntuaciones[0])):
        total = 0
        for j in range(len(puntuaciones)):
            total = total + puntuaciones[j][i]
        promedio = total / len(puntuaciones)
        if promedio < min_promedio:
            min_promedio = promedio
            jurado_estricto = i + 1
    print(f"El jurado más estricto es el Jurado {jurado_estricto} con un promedio de {min_promedio}.")

def Buscar_participante_por_nombre(participantes, puntuaciones): #8
    nombre_busqueda = input("Ingrese el nombre del participante a buscar: ")
    encontrado = False
    for i in range(len(participantes)):
        if participantes[i].lower() == nombre_busqueda.lower():
            print(f"Participante: {participantes[i]}")
            print(f"Puntuación Jurado 1: {puntuaciones[i][0]}")
            print(f"Puntuación Jurado 2: {puntuaciones[i][1]}")
            print(f"Puntuación Jurado 3: {puntuaciones[i][2]}")
            total = 0
            for j in range(len(puntuaciones[i])):
                total = total + puntuaciones[i][j]
            promedio = total / len(puntuaciones[i])
            print(f"Promedio general: {promedio}")
            encontrado = True
            break
    if not encontrado:
        print("Participante no encontrado.")

def Top_3(participantes, puntuaciones): #9
    promedios = []
    for i in range(len(participantes)):
        total = 0
        for j in range(len(puntuaciones[i])):
            total = total + puntuaciones[i][j]
        promedio = total / len(puntuaciones[i])
        promedios = agregar_a_lista(promedios, (participantes[i], promedio))
    n = len(promedios)
    for i in range(n):
        for j in range(0, n-i-1):
            if promedios[j][1] < promedios[j+1][1]:
                temp = promedios[j]
                promedios[j] = promedios[j+1]
                promedios[j+1] = temp
    print("Top 3 participantes:")
    for i in range(3):
        if i < len(promedios):
            print(f"{i+1}. {promedios[i][0]} - Promedio: {promedios[i][1]}")

def Orden_alfabetico_participantes(participantes, puntuaciones): #10
    n = len(participantes)
    participantes_ordenados = [participantes[i] for i in range(n)]
    for i in range(n):
        for j in range(0, n-i-1):
            if participantes_ordenados[j] > participantes_ordenados[j+1]:
                temp = participantes_ordenados[j]
                participantes_ordenados[j] = participantes_ordenados[j+1]
                participantes_ordenados[j+1] = temp
    print("Participantes ordenados alfabéticamente:")
    for participante in participantes_ordenados:
        index = -1
        for k in range(len(participantes)):
            if participantes[k] == participante:
                index = k
                break
        print(f"{participante} - Puntuación Jurado 1: {puntuaciones[index][0]}, Puntuación Jurado 2: {puntuaciones[index][1]}, Puntuación Jurado 3: {puntuaciones[index][2]}")