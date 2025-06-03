import os
from Funciones import (
    agregar_a_lista,
    Cargar_participantes,
    Cargar_puntuaciones,
    Mostrar_puntuaciones,
    Participantes_con_promedio_mayor_a_4,
    Participantes_con_puntuacion_mayor_a_7,
    Promedio_de_cada_jurado,
    Jurado_mas_estricto,
    Buscar_participante_por_nombre,
    Top_3,
    Orden_alfabetico_participantes
)

def limpiar_consola():
    os.system('cls')

def cargar_menu():
    ancho = 60
    print("\n" + "=" * ancho)
    print(" MENÚ DE OPCIONES ".center(ancho, "="))
    print("=" * ancho)
    print("1.  Cargar participantes")
    print("2.  Cargar puntuaciones")
    print("3.  Mostrar puntuaciones")
    print("4.  Participantes con promedio mayor a 4")
    print("5.  Participantes con promedio mayor a 7")
    print("6.  Promedio de cada jurado")
    print("7.  Jurado más estricto")
    print("8.  Buscar participante por nombre")
    print("9.  Top 3 participantes")
    print("10. Orden alfabético de participantes")
    print("0.  Salir")
    print("=" * ancho)

def main():
    participantes = []
    puntuaciones = []
    while True:
        cargar_menu()
        try:
            opcion = int(input("👉 Seleccione una opción: "))
        except ValueError:
            print("Opción inválida. Intente nuevamente.")
            continue

        limpiar_consola()

        if opcion == 1:
            participantes = Cargar_participantes()
            puntuaciones = []
        elif opcion == 2:
            if len(participantes) == 0:
                print("Primero debe cargar los nombres de los participantes.")
            else:
                puntuaciones = []
                for _ in range(len(participantes)):
                    # Usar agregar_a_lista para cumplir la restricción
                    puntuaciones = agregar_a_lista(puntuaciones, Cargar_puntuaciones())
        elif opcion == 3:
            if len(participantes) == 0 or len(puntuaciones) == 0:
                print("No hay datos cargados.")
            else:
                Mostrar_puntuaciones(participantes, puntuaciones)
        elif opcion == 4:
            if len(participantes) == 0 or len(puntuaciones) == 0:
                print("No hay datos cargados.")
            else:
                Participantes_con_promedio_mayor_a_4(participantes, puntuaciones)
        elif opcion == 5:
            if len(participantes) == 0 or len(puntuaciones) == 0:
                print("No hay datos cargados.")
            else:
                Participantes_con_puntuacion_mayor_a_7(participantes, puntuaciones)
        elif opcion == 6:
            if len(participantes) == 0 or len(puntuaciones) == 0:
                print("No hay datos cargados.")
            else:
                Promedio_de_cada_jurado(puntuaciones)
        elif opcion == 7:
            if len(participantes) == 0 or len(puntuaciones) == 0:
                print("No hay datos cargados.")
            else:
                Jurado_mas_estricto(puntuaciones)
        elif opcion == 8:
            if len(participantes) == 0 or len(puntuaciones) == 0:
                print("No hay datos cargados.")
            else:
                Buscar_participante_por_nombre(participantes, puntuaciones)
        elif opcion == 9:
            if len(participantes) == 0 or len(puntuaciones) == 0:
                print("No hay datos cargados.")
            else:
                Top_3(participantes, puntuaciones)
        elif opcion == 10:
            if len(participantes) == 0 or len(puntuaciones) == 0:
                print("No hay datos cargados.")
            else:
                Orden_alfabetico_participantes(participantes, puntuaciones)
        elif opcion == 0:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción fuera de rango.")

if __name__ == "__main__":
    main()