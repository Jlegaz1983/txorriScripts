edad = input('¿Cuantos años tienes?\n') #introduce datos por teclado
edad = int(edad)    #convierte de tip str a tipo int
if edad >= 18:
    print('Bienvenido al club.')
else:
    print('Eres menor de edad, no puedes pasar.')
