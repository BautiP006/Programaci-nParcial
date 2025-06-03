def input_Puntuación_del_Jurado(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("El número debe ser positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")

def input_nombre_participante():
    while True:
        nombre = input("Escribí tu nombre: ")
        valido = True
        for c in nombre:
            if not (
                (c >= 'a' and c <= 'z') or 
                (c >= 'A' and c <= 'Z') or 
                c == ' '
            ):
                valido = False
                break

        if valido:
            print("Nombre válido")
            return nombre
        else:
            print("Nombre inválido. Solo puede tener letras (sin acento) y espacios.")
