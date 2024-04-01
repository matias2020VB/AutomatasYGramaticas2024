import re
class Mail():
    __agregar = []
    __direccion = re.compile(("^[_a-z0-9-]+(.[_a-z0-9-]+)*@([a-z0-9-]{4,8})+(.[a-z0-9-]+)*(.[a-z]{2,4})$"))

    def setagrear(self, lista):
        self.__agregar = lista

    def setdireccion(self, direccion):
        self.__direccion = direccion

# Inciso A - Validación del correo electronico del usuario
    def correolist(self):
        print("VALIDACIÓN DE CORREO, PUNTO A")
        agregarcorreos = input("INGRESE SU CORREO ELECTRONICO: " u'')
        self.__agregar.append(agregarcorreos)

    def returnagregarcorreo(self):
        for correos in self.__agregar:
            match = self.__direccion.search(correos)
            print('{:<30}  {}'.format(correos, 'CORREO VALIDO' if match else 'CORREO NO VALIDO'))


token = Mail()
token.correolist()
token.returnagregarcorreo()