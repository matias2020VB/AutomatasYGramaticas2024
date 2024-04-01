# Solicitaremos al usuario que ingrese un string y validaremos si cumple con las siguientes condiciones:

string_argument = input("Ingrese un string: ")

# Creamos la funcion para "validar un string" pasandole como argumento un string de entrada.

def validate_string(string_input):

# Definiremos las condiciones de validacion: Alfanumerico, alfabetico, mayusculas, minusculas, digito y longitud.
# Inicializamos la variable de longitud en 0 para almacenar la longitud de la candena.
    
    string_long = 0 
    
# Inicializamos las variables de validacion en False.
    
    long_output = False
    validate_alnum = any(x.isalnum() for x in string_input) 
    validate_alpha = any(x.isalpha() for x in string_input)
    validate_upper = any(x.isupper() for x in string_input)
    validate_lower = any(x.islower() for x in string_input)
    validate_digit = any(x.isdigit() for x in string_input)
    validate_long = len(string_input)

# Necesitamos saber que si la longitud es mayor o igual a 8. La salida será True, de lo contrario False.

    if validate_long >= 8:
        long_output = True
    else:
        long_output = False

# Imprimiremos los resultados de cada validacion.

    print(validate_alnum)
    print(validate_alpha)
    print(validate_upper)
    print(validate_lower)
    print(validate_digit)
    print(long_output)

# Llamamos a la funcion validate_string pasandole como argumento el string ingresado por el usuario.

validate_string(string_argument)




