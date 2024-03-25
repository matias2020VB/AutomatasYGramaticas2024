def solve(expression):
    # Dividir la expresión en términos basados en los operadores
    terms = expression.split()
    
    # Inicializar el resultado como el primer término convertido a entero
    result = int(terms[0])
    
    # Iterar sobre los términos en la expresión
    for i in range(1, len(terms), 2):
        operator = terms[i]
        operand = int(terms[i+1])
        
        # Realizar la operación correspondiente y actualizar el resultado
        if operator == '+':
            result += operand
        elif operator == '*':
            result *= operand
    
    return result

def main():
    expression = input("Ingrese la expresión matemática: ")
    result = solve(expression)
    print("El resultado de la operación es:", result)

if __name__ == "__main__":
    main()
