
class Persona:

    def __init__(self, name="", age=0, dni=""):
        self._name = name
        self._age = age
        self._dni = dni

    @property
    def get_name(self):
        return self._name

    def set_name(self,new_name):
        self._name = new_name

    @property
    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age>0:
            self._age = new_age
        else:
            print("La nueva edad es invalida")

    @property
    def get_dni(self):
        return self._dni

    def set_dni(self, new_dni):
        if len(self._dni)==8:
            self._dni = new_dni
        else:
            print("El nuevo dni es erroneo")

    def mostrar(self):
        print(f"Nombre: {self._name}\nEdad: {self._age}\nDNI: {self._dni}")

    def es_mayor_de_Edad(self):
        if self._age>=18:
            return True
        else:
            return False


start_name= input("Ingrese su nombre: ")
start_age= int(input("Ingrese su edad: "))
start_dni= input("Ingrese su DNI: ")

if len(start_dni)==8 and start_age>-1:
    persona1 = Persona(start_name, start_age, start_dni)
    persona1.mostrar()
    print()
    if persona1.es_mayor_de_Edad():
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")

else:
    print("Ingreso un dato erroneamente")




