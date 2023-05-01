x = input('Introduce un número entero cualquiera...')
x = int(x)
if x < 0:
    print(f'{x} es menor que 0')
elif x > 0:
    print(f'{x} es mayor que 0')
else:
    print('x es 0')