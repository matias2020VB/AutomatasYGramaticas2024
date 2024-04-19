# Definición del AFD
afd = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q2', 'b': 'q1'},
    'q2': {'a': 'q2', 'b': 'q2'}
}

# Función para evaluar la cadena
def evaluar_cadena():
    cadena = input("Ingrese la cadena a evaluar: ")
    estado_actual = 'q0'
    for caracter in cadena:
        if caracter in afd[estado_actual]:
            estado_siguiente = afd[estado_actual][caracter]
            print(f"[{estado_actual}] -- ({caracter}) --> [{estado_siguiente}]")
            estado_actual = estado_siguiente
        else:
            print(f"[{estado_actual}] -- ({caracter}) --> [Rechazado]")
            return "La cadena no es aceptada"
    if estado_actual == 'q2':
        return "La cadena es aceptada"
    else:
        return "La cadena no es aceptada"

# Ejecución del programa
resultado = evaluar_cadena()
print(resultado)
