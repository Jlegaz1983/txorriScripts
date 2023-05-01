def Sumar():
    sum1 = int(input("Sumando uno:"))
    sum2 = int(input("Sumando dos:"))
    print("La Suma es:",sum1 + sum2)

def Restar():
    minuendo = int(input("Minuendo:"))
    sustraendo = int(input("Sustraendo:"))
    print("La Resta es:",minuendo - sustraendo)

def Multiplicar():
    multiplicando = int(input("Multiplicando:"))
    multiplicador = int(input("Multiplicador:"))
    print("La Multiplicación es:",multiplicando * multiplicador)

def Dividir():
    dividendo = int(input("Dividiendo:"))
    divisor = int(input("Divisor:"))
    print("La División es:", dividendo / divisor)
    
def Calculadora():
    fin = False
    while not(fin):
        opc = int(input("Opción:"))
        if(opc==1):
            Sumar()
        elif(opc==2):
            Restar()
        elif(opc==3):
            Multiplicar()
        elif(opc==4):
            Dividir()
        elif(opc==5):
            print("Gracias por usar la calculadora evolutiva.")
            fin = True

print("""
      ***************
      **Calculadora**
      ***************
      
      Menu
      
      1)Suma
      2)Resta
      3)Multiplicación
      4)División
      5)Salir\n""")

Calculadora()
