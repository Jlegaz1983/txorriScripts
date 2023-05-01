resultado = None
x = 10
y = 2
if y != 0:
    resultado = x / y
else:
    resultado = f'No se puede dividir {x} entre {y}'
print(resultado)

#diferente manera de solucionar el mismo problema.
#la segunda manera da una excepción.

resul = None
xx = input('Introduce un número\n')
xx = int(xx)
yy = input('Introduce un número\n')
yy = int(yy)
if y == 0:
    resul = f'No se puede dividir {xx} entre {yy}'
else:
    resul = xx / yy
print(resul)