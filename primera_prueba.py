lista = [0,1,2,3,4,5,6,7,8,9]
x = 0
print(lista)
print("La lista contiene",len(lista),"números.")

for x in lista:
    lista.remove(x)
    x = x + 1
    print(lista)
    print("Ahora tiene",len(lista),"números.")

    
