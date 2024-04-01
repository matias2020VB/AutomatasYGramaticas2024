import re
ip = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)$")

print("VALIDACION DE IPV4, PUNTO C")
agregardireccion = [input("INGRESE SU DIRECCION IPV: ")]

for direccionip in agregardireccion:
    match = ip.search(direccionip)
    print('{:<30}  {}'.format(direccionip, 'DIRECCION DE IP VALIDA' if match else 'DIRECCION DE IP NO VALIDA'))