""""
lista = []
salir = False

while not salir:
    num = int(input("Dame un número: "))

    if num != 0:
        lista.append(num)
    else:
        salir = True
        lista.sort(reverse=True)
        print(lista)
       
cadena = input("¿Que quieres saber?: ")

print(cadena)

lista = []

for c in cadena:
    if(c != " "):
        lista.append(c)

print(lista)



cadena = input("Dame una cadena: ")

print(cadena)

lista = []

for c in cadena:
    if(c not in lista):
        lista.append(c)

for e in lista:
    print(e)
"""


