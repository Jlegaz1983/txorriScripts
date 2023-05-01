x = input('Ingrese la coordenada X.\n')
x = int(x)
y = input('Ingrese la coordenada Y\n')
y = int(y)
if x > 0 and y > 0:
    print('Primer cuadrante.')
elif x < 0 and y > 0:
    print('Segundo cuadrante.')
elif x < 0 and y < 0:
    print('Tercer cuadrante.')
elif x > 0 and y < 0:
    print('Cuarto cuadrante.')