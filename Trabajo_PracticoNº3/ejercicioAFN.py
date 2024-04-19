afn = {
    'q0': {'a': ['q1'], 'b': ['q1'], 'ε': ['q1']},  # Transiciones desde el estado q0
    'q1': {'a': ['q1'], 'b': ['q1']}  # Transiciones desde el estado q1
}

# Función para evaluar la cadena en el AFN
def evaluar_cadena(cadena):
    estado_actual = 'q0'  # Estado inicial del autómata
    for simbolo in cadena:
        if simbolo in afn[estado_actual]:  # Verificar si el símbolo es parte de las transiciones del estado actual
            estado_siguiente = afn[estado_actual][simbolo][0]  # Obtener el estado siguiente según la transición
            print(f"[{estado_actual}] -- ({simbolo}) --> [{estado_siguiente}]")  # Mostrar la transición
            estado_actual = estado_siguiente  # Actualizar el estado actual con el estado siguiente
        else:
            print(f"[{estado_actual}] -- ({simbolo}) --> [Rechazado]")  # Mostrar que la transición es rechazada
            print("La cadena NO es aceptada por el autómata.")  
            return False  # Retornar False porque la cadena no es aceptada
    
    if estado_actual == 'q1':  # Verificar si el estado actual es un estado de aceptación
        print("La cadena SI es aceptada por el autómata.")  
        return True  # Retornar True porque la cadena es aceptada
    else:
        print("La cadena NO es aceptada por el autómata.")  #
        return False  

# Función principal para recibir la cadena por stdin y llamar a evaluar_cadena
def main():
    cadena = input("Ingrese la cadena a evaluar: ")  
    evaluar_cadena(cadena)  # Llamar a la función evaluar_cadena con la cadena ingresada

# Ejecución del programa principal
if __name__ == "__main__":
    main()  
