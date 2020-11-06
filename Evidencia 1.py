import shutil
import sys
SEPARADOR = ("*"*20)

def menu_principal():
    print("\n- MENÚ DEL SISTEMA -")
    print("[1] Copiar un documento entre directorios del sistema")
    print("[2] Mover un documento entre directorios del sistema")
    print("[3] Aplicacion de Estructuras de Datos 'Listas' Y 'Tuplas'")
    print("[4] Salir")



ciclo = True
while ciclo:
    continuar = True
    menu_principal()
    opcion = int(input("Eliga el número de la opción que desee: "))
    
    if opcion == 1:
        
        while continuar:
            print("Proporcione los parametros para copiar el documento a un nuevo directorio.")
            
            Parametro_1 = str(input("Ingrese el nombre de el archivo del que se copiaran los datos: "))
            Parametro_2 = str(input("Ingrese el nombre de el archivo que recibira los nuevos datos: "))
            shutil.copy(Parametro_1,Parametro_2)
            print(f"Se ha copiado con exito los datos de archivo {Parametro_1} al archivo {Parametro_2}")
            seguir = int(input("¿Desea copiar otro archivo en otro directorio?, 1 para seguir --- 0 para terminar: "))
            
            if seguir == 0:
                continuar = False
     
    if opcion == 2:
        
        while continuar:
            print("Proporcione los parametros para mover el documento a un nuevo directorio.")
            
            Parametro_1 = str(input("Ingrese el nombre del archivo que se movera de directorio: "))
            Parametro_2 = str(input("Ingrese el nombre del directorio como destino: "))
            shutil.move(Parametro_1,Parametro_2)
            print(f"Se ha movido con exito el archivo '{Parametro_1}' a la carpeta '{Parametro_2}'")
            seguir = int(input("¿Desea mover otro archivo en otro directorio?, 1 para seguir --- 0 para terminar: "))
            
            if seguir == 0:
                continuar = False 
    if opcion == 3:
        
        while continuar:
            print("A continuacion ingrese 5 valores enteros (en desorden) para llenar la lista que se creara.")
            lista=[]
            for x in range(5):
                valor = int(input('Ingrese 5 valores enteros para la lista: '))
                lista.append(valor)
            print("Lista creada",lista)
            
            lista_ordenada = sorted(lista)
            print(f"lista original = {lista}, y la version ordenada es {lista_ordenada}")
            print(SEPARADOR)
            lista_uno_al_doble = [valor * 2 for valor in lista]
            print(f"Aplicando comprension de listas, resultado x 2 a cada valor lista original = {lista_uno_al_doble}")
            print(SEPARADOR)
            tupla = (tuple(lista))
            print(SEPARADOR)
            print("Tupla creada en base a los mismo valores de la lista: ",tupla)
            print(type(tupla))
            print(SEPARADOR)
            print("Comparacion de consumo de recursos entre 'Lista' y 'Tupla'")
            print(f"La lista tiene tiene un tamaño de {sys.getsizeof(lista)} bytes")
            print(f"La tupla tiene tiene un tamaño de {sys.getsizeof(tupla)} bytes")
            
            seguir = int(input("¿Desea nuevamente probar la aplicacion de estructuras de 'Listas' y 'Tuplas' ?(1 para seguir --- 0 para terminar): "))
            
            if seguir == 0:
                continuar = False 
    elif opcion == 4:
        ciclo = False
print("PROGRAMA CONCLUIDO")            
