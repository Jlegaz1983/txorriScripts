#Leer un archivo entero
with open('C:/Users/Jlega/Documents/py_carpeta/fichero2.txt', 'r') as f:
    contenido = f.read()
    print(contenido)
    print('\n') #caracter escape
#Leer un archivo linea a linea
with open('C:/Users/Jlega/Documents/py_carpeta/fichero2.txt', 'r') as fi:
    for linea in fi:
        print(linea)
