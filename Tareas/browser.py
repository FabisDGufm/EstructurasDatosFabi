# Browser de Fabi
from memory_profiler import profile

back = ["Amazon", "Docs"]
forward = ["YouTube"]
actual = "MiU"

@profile
def main():
     print("Hola, bienvenido a la simulación de tu browser")
     while True:
        acc = menu()
        if acc == 1:
            if (len(back) == 0):
                print("No hay pestañas anteriores")
            else:
                print("Regresando a la pestaña anterior...")
                regresar()
        elif acc == 2:
            if (len(forward) == 0):
                print("No hay pestañas siguientes")
            else:
                print("Dirigiéndonos a la pestaña siguiente...")
                adelantar()
        elif acc == 3:
            print("Refrescando pestaña...")
        elif acc == 4:
             print("Saliendo de la simulación...")
             print("Hasta pronto :)")
             return False
        else:
            print("Formato o número no válido, intentar de nuevo")
     

def regresar():
    global actual
    forward.append(actual)
    actual = back.pop()

def adelantar():
    global actual
    back.append(actual)
    actual = forward.pop()
        
def menu():
     print("Te encuentras en a pestaña de: " + actual)
     print()
     print("""Deseas:
    1. Regresar a la pestaña anterior <--
    2. Ir a la pestaña siguiente -->
    3. Refrescar pestaña
    4. Salir x
    Ingresa el número de la acción que deseas realizar (ej: 1):""")
     accion = int(input())
     return accion

main()