from claseManejadorAlumno import Manejador
from ClaseMenuejercico5 import Menu
import os


def test ():
    unManejador=Manejador()
    unManejador.testAlumno()
    a=5
    d=4
    unManejador.listar(a,d)
    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Inciso 1\n2. Inciso 2\n3. Salir")
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        menu.opcion(op, unManejador)
        salir = op == 3
    print(salir)
    
    

if __name__=="__main__":
    test()    