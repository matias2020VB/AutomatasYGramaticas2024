import re

# Inicializamos una variable llamada 'ip' para validar las direcciones IP

ip = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)$")

# Inciso C - Validamos la dirección IP

print("Validacion de una IP - IPv4")
add_address = [input("Ingrese una direccion IP con el protocolo IPv4: ")]

# Utilizamos el bucle for para recorrer la lista de direcciones IP ingresadas por teclado.
# Utilizamos el método search() para buscar la dirección IP en la lista de direcciones IP ingresadas.

for ip_address in add_address:
    match = ip.search(ip_address)
    print('{:<30}  {}'.format(ip_address, 'Direccion de IP correcta' if match else 'Direccion de IP incorrecta'))