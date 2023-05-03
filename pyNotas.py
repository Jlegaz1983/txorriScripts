listaNotas = []
salir = False
print('''
          *********
          *pyNotas*
          *********
          
          1) Nota nueva
          2) Ver notas
          3) Borrar nota
          4) Borrar todas
          5) Salir
          ''')
while not salir:
    indice = int(input(""))
    if indice == 1:
        nota = input("Nota nueva:\n")
        listaNotas.append(nota)
    elif indice == 2:
        print("Notas:")
        for i in listaNotas:
            print(i)
    elif indice == 3:
        print(len(listaNotas), "notas guardadas\n")
        indiceBorrar = int(input("Selecciona la nota a borrar: "))
        del listaNotas[indiceBorrar - 1]
    elif indice == 4:
        listaNotas = []
        print("No hay ninguna nota en memoria")
    else:
        salir = True
        print("Gracias por confiar en pyNotas\nCreado por Jlegaz83")