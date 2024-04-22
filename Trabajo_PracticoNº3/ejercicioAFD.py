class Automata():
    def __init__(self, text):
        self.__text = text
        self.afd = {
            'q0': {'a': 'q1', 'b': 'q0'},  # Transiciones desde el estado q0
            'q1': {'a': 'q2', 'b': 'q1'},  # Transiciones desde el estado q1
            'q2': {'a': 'q2', 'b': 'q2'}   # Transiciones desde el estado q2
        }

    def table(self):
        print('|--------|----------------------|\n|        |  Simbolo de entrada  |\n| Estado |-----------|----------|\n|        |     a     |     b    |')
        print('|--------|-----------|----------|\n|  Q0    |    Q1     |    Q2    |\n|  Q1    |    Q1     |    Q2    |\n|  Q2    |    Q1     |    Q2    |')
        print('|--------|-----------|----------|')

    def secuencias(self):
        aceptacion = ['q2']
        estado_actual = 'q0'
        print('Estado:', estado_actual)
        for caracter in self.__text:
            if caracter in self.afd[estado_actual]:
                print('Caracter:', caracter)
                estado_siguiente = self.afd[estado_actual][caracter]
                print(f'Transición de {estado_actual} a {estado_siguiente}')
                estado_actual = estado_siguiente
            else:
                print(f'Caracter no válido: {caracter}')
                print('La cadena NO es aceptada por el autómata.\n')
                return True
            print('Estado:', estado_actual)

        if estado_actual in aceptacion:
            print("La cadena SI es aceptada por el autómata.")
            return False
        else:
            print('La cadena NO es aceptada por el autómata.\n')
            return True

    def validacion(self):
        validos = {'a', 'b'}
        invalidos = [caracter for caracter in self.__text if caracter not in validos]
        if invalidos:
            print('Caracteres inválidos:', invalidos)
            return False
        return True

def main():
    text = input("Ingrese la cadena a evaluar: ")
    AFD = Automata(text)
    AFD.table()
    AFD.secuencias()
    AFD.validacion()

if __name__ == "__main__":
    main()
