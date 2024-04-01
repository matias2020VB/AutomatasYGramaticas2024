import re

# Inicializamos las expresiones regulares para validar las URL

url_1 = re.compile("^(https?://)?(www\.)?([a-zA-Z0-9/.-])+[a-zA-Z0-9]\.(com|ar|net|org|edu\.ar|edu\.com|edu\.org)+([/a-zA-Z0-9/])*$")
url_2 = re.compile("^(www\.)?([a-zA-Z0-9/.-])+[a-zA-Z0-9]\.(com|es|ar|net|org|um\.edu\.ar|edu\.ar|edu\.com|edu\.org|cl|co|cn|ae|au|br|ca|nz)+\.(ar|cl|co|cn|ae|au|br|ca|nz|es)+([/a-zA-Z0-9/])*$")
url_3 = re.compile("^([a-zA-Z0-9/.-])+[a-zA-Z0-9]\.(com|es|co|ar|net|org|um|edu)+\.(ar|cl|co|cn|ae|au|br|ca|nz|es|edu)+\.(ar|cl|co|cn|ae|au|br|ca|nz|es|edu)+([/a-zA-Z0-9/])*$")

# Inciso B - Validamos la URL

print("Validacion de una URL")
add_url = [input("Ingrese una URL por teclado: " u'')]

# Utilizamos el bucle for para recorrer la lista de URL ingresadas por teclado.
# Utilizamos el método search() para buscar la URL en la lista de URL ingresadas.

for page in add_url:
    match_one = url_1.search(page)
    match_two = url_2.search(page)
    match_tree = url_3.search(page)

# Utilizo el 'if' para validar si la URL ingresada es válida o no.

    if match_one or match_two or match_tree:
        print('{:<30}  {}'.format(page, 'Usted ha ingresado una URL válida'))
    else: 
        print('{:<30}  {}'.format(page, 'Usted ha ingresado una URL inválida'))
