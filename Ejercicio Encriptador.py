# Ejercicio Encriptacion

user_chain = str(input("Ingrese la cadena a encriptar: "))

n = int(input("Ingrese el valor de n: "))

# Creamos la funcion de encriptacion

def encrypt_chain(user_chain, n):
    # Creamos una cadena vacia para almacenar la cadena encriptada.
    encrypted_chain = ""
    
    # Recorremos la cadena ingresada por el usuario y le sumamos el valor de n a cada caracter.
    for i in user_chain:
        # Si el caracter es un espacio, lo dejamos igual.
        if i == " ":
            encrypted_chain += i
        else:
            # Concatenamos cada caracter encriptado a la cadena vacia.
            encrypted_chain += chr(ord(i) + n)

# Retornamos la cadena encriptada.  
    return encrypted_chain

# Imprimimos la cadena encriptada.
print(encrypt_chain(user_chain=user_chain, n=n))