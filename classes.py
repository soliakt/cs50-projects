import sys

class Point():
    # Cada def es una función
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # el __init__ es el constructor
    # esto es como poner this.x = x o this.y = y

p = Point(2, 4)
print(p.x)
print(p.y)


class Flight():
    # Cada def es una función
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def addPassenger(self, nameIn):
        if not self.seatsAvailable(): # Otra forma: if self.seatsAvailable() == 0:
            return False
        else:
            self.passengers.append(nameIn)
            return True

    def seatsAvailable(self):
        return self.capacity - len(self.passengers)

ryanair = Flight(3)

pasajeros = ["Víctor", "Marcos", "Lucas", "Martín"]

for person in pasajeros:
    if ryanair.addPassenger(person): 
        # Otra forma: 
        # success = ryanair.addPassenger(person)
        # if success == True:
        print(f"We've added {person} succesfully")
    else:
        print(f"We coultn't add {person} because flight is full")

'''
DECORADOR: es una funcion que coge otra función como input y devuelve la funcion modificada
Sirven para modificar una función. 
OJO, repito: un decorador coge una función y devuelve OTRA. 
Por eso necesitamos crear un envoltorio (wrapper)
'''

def anuncio(funcion):
    # El decorador anuncio está cogiendo la función funcion y está creando una nueva función
    # que anuncia el antes y el después de cuándo la función se ha ejecutado
    def wrapper():
        print("Bienvenido a Marmarela! ")
        if funcion() > 17:
            print("Bienvenido a bordo camarada!")
        else:
            print("¡¡Debes ser mayor de edad para estar aquí!!")
    return wrapper # Esto es lo que nos devuelve.

# No entiendo porqué se imprime antes el holaaaa que lo demás
print("Holaaaa")


@anuncio
def preguntarEdad():
    try:
        edad = int(input("Introduce tu edad: "))
    except ValueError:
        print("No es un número válido")
        sys.exit(1)
    return edad

preguntarEdad()


alumnos = [
    {   
        "Nombre": "Víctor", 
        "Apellido": "Gimeno",
        "Grado": "ADE"
    },
    {
        "Nombre": "Clara", 
        "Apellido": "Verdeguer",
        "Grado": "Enfermería"
    },
    {
        "Nombre": "Pablo", 
        "Apellido": "Martinez",
        "Grado": "DAW"
    }
]

print(alumnos)


def nombreAlumno(alumno):
    return alumno["Nombre"]

print("Nuevo orden")
alumnos.sort(key = nombreAlumno)
#Otra forma alumnos.sort(key = lambda alumno: alumno[Nombre]) Con esto no hace falta 
# crear la funcion nombreAlumno
# lambda es la propia función que coge un alumno como input y devuelve el nombre
'''
Cuando se llama al método sort() en una lista, el parámetro key acepta una función 
que toma un elemento de la lista como argumento y devuelve un valor que se utilizará para comparar y ordenar los elementos
'''
print(alumnos)