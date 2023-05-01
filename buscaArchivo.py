import os

ruta = 'C:\\Users\\Jlega\\jlega:local\\txts'

for raiz, directorios, archivos in os.walk(ruta):
    for archivo in archivos:
        if archivo.endswith('.txt'):
            print(os.path.join(raiz, archivo))
            