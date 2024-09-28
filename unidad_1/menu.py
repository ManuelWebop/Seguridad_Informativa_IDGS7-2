import os
import subprocess

'''
desarrollado por Manuel Francisco Amavizca Barrios.
'''

def limpiar_pantalla():
    os.system("clear")

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, check=True)
        return resultado
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {comando}")
        print(f"Detalles: {e}")

print("Sistema para pruebas de seguridad informatica")
print("Version 1.0")
print("Desarrollado por: Amavizca Barrios Manuel Francisco")

x = True

limpiar_pantalla()

while x:
    print("\nOpcion 1: Encontrar IP (Socket).")
    print("Opcion 2: Encontrar IP (Python).")
    print("Opcion 3: Encontrar subdominios.")
    print("Opcion 4: Banner Grabbing.")
    print("Opcion 5: Wad.")
    print("Opcion 6: Escaneo de Puertos.")
    print("Opcion 7: Salir.")
    
    try:
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            dominio=input("Obtener IP: ")
            comando = f"py getip.py -t {dominio}"
            ejecutar_comando(comando)
            input("Finalizado")
            limpiar_pantalla()

        elif opcion == 2:
            dominio = input("Obtener IP: ")
            comando = f"py getip2.py -t {dominio}"
            print("Obtener IP")
            ejecutar_comando(comando)
            input("Finalizado")
            limpiar_pantalla() 

        elif opcion == 3:
            victima = input("Ingrese el dominio: ")
            print("Encontrar subdominios")
            comando = f"py subdominios.py -t {victima}"
            ejecutar_comando(comando)
            input("Presione Enter para continuar...")
            limpiar_pantalla()

        elif  opcion == 4:
            victima = input("Ingrese el dominio: ")
            puerto = input("Ingrese el puerto: ")
            print("Banner Grabbing")
            comando = f"py bannergraby.py -t {victima} -p {puerto}"
            ejecutar_comando(comando)
            input("Presione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == 5:
            print("Wad")
            input("Presione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == 6:
            print("Escaneo de Puertos")
            input("Presione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == 7:
            print("Saliendo del sistema...")
            x = False
        else:
            print("Opcion no valida, intenta de nuevo.")
    
    except ValueError:
        print("Error: Ingrese un numero valido.")
