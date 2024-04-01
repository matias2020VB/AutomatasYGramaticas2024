# Debo pedirle al usuario una expresion matematica para que pueda realizar la operacion correspondiente.

expression_user = input("Ingrese la expresión matemática: ")

# Definiré una funcion que sea multiplicacion. 

def multiplication(multiplicator):

# Guardaré la cadena de entrada en una variable nueva.
    
    mult = multiplicator

# Luego de eso, dividiré la cadena 'mult' en una lista llamada 'list_mult' usando el operador '*'. 
# Por ejemplo si tengo "2 * 3" la lista será ["2", "*", "3"].

    list_mult = mult.split("*")
    
# Una vez listada la cadena, lo que haré es convertir la lista en un entero. Esto es necesario porque
# El método split() devuelve una lista de cadenas, por lo que necesitamos convertir los elementos de la lista en enteros.
# Por lo tanto si list_mult = ["2", "*", "3"], la lista se convertirá en [2, 3].

    list_mult = [int(x) for x in list_mult]

# Luego inicializaré una variable llamada 'mult_result' en 1. Esto lo necesito porque si multiplico cualquier número por 1, el resultado será el mismo número.
    
    mult_result = 1

# Ahora lo que haré es recorrer la lista 'list_mult' y multiplicar cada elemento de la lista por 'mult_result', por ejemplo si tengo [2, 3], el resultado será 6.
# return mult_result me devolverá el resultado de la multiplicacion.

    for element in list_mult:
        mult_result *= element
    return mult_result

# Procederé a crear la funcion solve_expression que reciba como argumento la expresion matematica ingresada por el usuario y me permitirá realizar la operacion correspondiente.

def solve_expression(operation):
# Inicializaré una variable llamada 'operation' para almacenar la operacion ingresada por el usuario.
# Donde utilizaré el metodo replace() para eliminar los espacios en blanco de la cadena de entrada.
# Esto es importante para que no haya espacios en blanco que puedan interferir con la interpretacion de la operación.
    
    operation = operation.replace(" ", "")
    
# Luego dividiré la cadena de operacion en una lista de elementos separados por el operador '+' llamada 'operation_list'.
# Por ejemplo si tengo "2+3+4", la lista será ["2", "+", "3", "+", "4"].
    
    operatator_list = operation.split("+")
    
# Inicializare una variable llamada mult_result en 0. Almacenaré temporalmente cualquier operacion de multiplicacion encontrada en la lista operadora(operator_list).

#    mult = 0
    
# Iteramos cada elemento de la lista 'operator_list' Utilizando un bucle for, contando 

    for i in range(0, len(operatator_list)):
        
# Inicializamos una variable llamada elemnt para almacenar el elemento actual de la lista 'operator_list'.        
        elemnt = operatator_list[i]
        
# Verificamos si el elemento actual contiene el operador de multiplicacion '*'.            
        if "*" in elemnt:
# Inicializo una variable llamada result 
            
            result = multiplication(elemnt)
            
# Si el operador de la multiplicacion '*' está presente en 'operator_list', llamamos a la funcion 'multiplication' para realizar la operacion de multiplicacion.
            
            operatator_list[i] = result

# Ahora lo que haremos es convertir los elementos de la lista 'operator_list' en enteros.

    operatator_list = [int(x) for x in operatator_list]
    
# Crearé una variable llamada 'final_result' que calculará la suma de todos los elementos en la lista 'operator_list', que son
# los resultados de las operaciones de multiplicacion y las operaciones de suma.

    final_result = sum(operatator_list)

# Imprimimos el resultado final.
    
    print(f"El resultado final de la operacion es: {final_result}")

# Llamamos a la funcion 'solve_expression' pasandole como argumento la expresion matematica ingresada por el usuario.
solve_expression(expression_user)