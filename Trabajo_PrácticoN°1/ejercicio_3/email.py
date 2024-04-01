import re

# Creamos la clase Mail con los atributos __add y __address para almacenar la lista de correos y la expresión regular para validar el correo electrónico.
class Mail():
    __add = []
    __address = re.compile(("^[_a-z0-9-]+(.[_a-z0-9-]+)*@([a-z0-9-]{4,8})+(.[a-z0-9-]+)*(.[a-z]{2,4})$"))

# Creamos los métodos setAdd y setAddress para asignar valores a los atributos __add y __address.

    def setAdd(self, list):
        self.__add = list

    def setAddress(self, address):
        self.__address = address

# Inciso A - Validación del correo electronico del usuario.

# Creamos la funcion mailList para que el usuario ingrese su correo electrónico y lo almacene en la lista __add. Utilizando el metodo.append() para agregar el correo a la lista.
    
    def mailList(self):
        print("Validacion del Mail del usuario")
        add_mail = input("Ingrese su mail: " u'')
        self.__add.append(add_mail)
# Creamos la funcion returnAddMail para recorrer la lista de correos almacenados en __add y validar si el correo es correcto o no 
# utilizando el método search() para buscar el correo en la lista de correos almacenados.

    def returnAddMail(self):
        for correos in self.__add:
            match = self.__address.search(correos)
            print('{:<30}  {}'.format(correos, 'CORREO VALIDO' if match else 'CORREO NO VALIDO'))

# Creamos un objeto token de la clase Mail y llamamos a los métodos mailList y returnAddMail.

token = Mail()
token.mailList()
token.returnAddMail()