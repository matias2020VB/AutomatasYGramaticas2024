# Esta función toma un string como entrada y valida si cumple con ciertas condiciones.
# Devuelve una lista de booleanos indicando si se cumplen las condiciones o no.
def validate_string(s):
    # Lista de condiciones a verificar
    conditions = [
        any(char.isalnum() for char in s),  # Verifica si hay al menos un carácter alfanumérico
        any(char.isalpha() for char in s),  # Verifica si hay al menos una letra
        any(char.isupper() for char in s),  # Verifica si hay al menos una letra mayúscula
        any(char.islower() for char in s),  # Verifica si hay al menos una letra minúscula
        any(char.isdigit() for char in s),  # Verifica si hay al menos un dígito
        len(s) >= 8  # Verifica si la longitud del string es 8 o mayor
    ]
    return conditions

# Esta función principal solicita al usuario que ingrese un string por consola,
# luego llama a la función validate_string con ese string y muestra los resultados.
def main():
    user_input = input("Ingrese un string para validar: ")  # Solicita al usuario que ingrese un string
    result = validate_string(user_input)  # Llama a la función validate_string con el string ingresado por el usuario
    print("Resultados de validación:")  # Imprime un mensaje indicando los resultados de la validación
    for condition in result:  # Itera sobre cada condición en los resultados
        print(condition)  # Imprime el resultado de cada condición

if __name__ == "__main__":
    main()  # Llama a la función main si este script es ejecutado directamente




