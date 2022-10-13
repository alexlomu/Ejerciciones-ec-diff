from ejercicios import *

def iniciar():
    while True:

        print("========================")
        print("  Bienvenido al menú  ")
        print("========================")
        print("  Selecciona la ecuación que quieras resolver  ")        
        print("========================")        
        print("[1] EJERCICIO 1 ")
        print("[2] EJERCICIO 2 ")
        print("[3] EJERCICIO 3 ")
        print("[4] EJERCICIO 4 ")
        print("[5] Salir del menú ")
        print("===================")


        opcion = input("> ")

        if opcion == "1":
            ej1()
        
        elif opcion =="2":
            ej2()
        
        elif opcion =="3":
            ej3()

        elif opcion =="4":
            ej4()
        
        elif opcion == "5":
            break

if __name__ == "__main__":
    iniciar()