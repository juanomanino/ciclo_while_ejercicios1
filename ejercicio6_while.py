# Bucle While: Ejemplo de Menú

num=int(input("Menú: 1(ver números), 0(Salir) "))

while num!=0:
    x=0
    while x<10:
        print("El valor de X es: ",x)
        x +=1
    
    print("Saliendo...")
    num=int(input("Menú: 1(ver números), 0(Salir) "))


print("Gracias")
