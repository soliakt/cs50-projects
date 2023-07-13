print("Hello, world!")

name = input("Name: ")
print("Hello, " + name)
print(f"Hello, {name}")



n = input("Number: ")

if n.isdigit():
    n = int(n)
    if n > 0:
        print(f"{n} is positive")
    elif n < 0:
        print(f"{n} is negative")
    else: 
        print("Number is zero")
else:
    print("No es un número entero válido.")

#Define a list of names
names = ["Víctor", "Pablo", "Paula", "María"]

print(names)
ans = int(input("Wanna add any other name? Press 1 for yes, 0 for no: "))
if ans == 1:
    newName = input("Name to append: ")
    names.append(newName)
print(names)

names.sort()
print(names)

ciclos = {
    "Víctor": "ADE", 
    "Marta": "DAW"
    }

print("Víctor estudia " + ciclos["Víctor"])

addNew = int(input("Quieres añadir otro alumno? 1 YES 0 NO: "))
if addNew == 1:
    nombreAdd = input("Ingresa el nombre: ")
    cicloAdd = input("Ingresa el ciclo: ")
    ciclos[nombreAdd] = cicloAdd
    print(ciclos)
