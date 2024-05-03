class Automata():
    def __init__(self, texto):
        self.__texto = texto  # Inicializa el autómata con un texto de entrada

    def tabla(self):
        # Imprime la tabla de transiciones del autómata
        print('|--------|----------------------|\n|        |  Símbolo de entrada  |\n| Estado |-----------|----------|\n|        |     a     |     b    |')
        print('|--------|-----------|----------|\n|  Q0    |    Q1     |    Q2    |\n|  Q1    |    Q1     |    Q2    |\n|  Q2    |    Q1     |    Q2    |')
        print('|--------|-----------|----------|')

    def secuencias(self):
        aceptacion = ['Q1','Q2']  # Define los estados de aceptación
        estado_actual = 'Q0'  # Establece el estado inicial
        print('Estado:', estado_actual)  # Imprime el estado actual
        for i in range(len(self.__texto)):
            if estado_actual == 'Q0':
                print('Carácter:', self.__texto[i])  # Imprime el carácter actual
                if self.__texto[i] == 'a':
                    print('Transición de Q0 a Q1')  # Imprime la transición
                    estado_actual = 'Q1'  # Actualiza el estado actual
                if self.__texto[i] == 'b':
                    print('Transición de Q0 a Q2')  
                    estado_actual = 'Q2'  
                elif estado_actual == 'Q1':
                    print('Carácter:', self.__texto[i])  
                    if self.__texto[i] == 'a':
                        print('Transición de Q1 a Q1')  
                        estado_actual = 'Q1'  
                    if self.__texto[i] == 'b':
                        print('Transición de Q1 a Q2')  
                        estado_actual = 'Q2'  
            elif estado_actual == 'Q2':
                print('Carácter:', self.__texto[i])  
                if self.__texto[i] == 'a':
                    print('Transición de Q2 a Q1')  
                    estado_actual = 'Q1'  
                if self.__texto[i] == 'b':
                    print('Transición de Q2 a Q2')  
                    estado_actual = 'Q2'  
            print('Estado:', estado_actual)  # Imprime el estado actual después de cada transición

        if estado_actual in aceptacion:
            print('ESTADO DE ACEPTACIÓN ALCANZADO')  # Imprime si el estado de aceptación se alcanza
            return False
        else:
            print('NO SE ALCANZA UN ESTADO DE ACEPTACIÓN. CADENA NO VÁLIDA.\n')  # Imprime si no se alcanza un estado de aceptación
            return True

    def validacion(self):
        validos = ['a', 'b']  # Define los caracteres válidos
        for i in range(len(self.__texto)):
            if self.__texto[i] not in validos:
                print('CARÁCTER INVÁLIDO:', self.__texto[i])  # Imprime caracteres inválidos
                return False
        return True

def main():
    texto = input("INTRODUCIR CARÁCTER:")  
    AFD = Automata(texto)  # Crea un objeto de la clase Automata con el texto proporcionado
    AFD.tabla()  # Imprime la tabla de transiciones del autómata
    AFD.secuencias()  # Ejecuta la simulación de secuencias en el autómata
    AFD.validacion()  # Valida si el texto contiene caracteres válidos

if __name__ == "__main__":
    main()  
