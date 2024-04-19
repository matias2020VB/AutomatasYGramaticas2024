afd = {
    'q0': {'a': 'q1', 'b': 'q0'},  # Transiciones desde el estado q0
    'q1': {'a': 'q2', 'b': 'q1'},  # Transiciones desde el estado q1
    'q2': {'a': 'q2', 'b': 'q2'}   # Transiciones desde el estado q2
}

# Función para evaluar la cadena en el AFD
def evaluar_cadena():
    cadena = input("Ingrese la cadena a evaluar: ")  
    estado_actual = 'q0'  # Estado inicial del autómata
    for caracter in cadena:
        if caracter in afd[estado_actual]:  # Verificar si el caracter es parte de las transiciones del estado actual
            estado_siguiente = afd[estado_actual][caracter]  # Obtener el estado siguiente según la transición
            print(f"[{estado_actual}] -- ({caracter}) --> [{estado_siguiente}]")  # Mostrar la transición
            estado_actual = estado_siguiente  # Actualizar el estado actual con el estado siguiente
        else:
            print(f"[{estado_actual}] -- ({caracter}) --> [Rechazado]")  # Mostrar que la transición es rechazada
            return "La cadena no es aceptada"  
    if estado_actual == 'q2':  # Verificar si el estado actual es un estado de aceptación
        return "La cadena es aceptada"  
    else:
        return "La cadena no es aceptada"  

# Ejecución del programa
resultado = evaluar_cadena()  
print(resultado)  
