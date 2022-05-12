# Bucle While

num=int(input("Ingrese un número positivo: "))

while num<0:
    print("Este es un número negativo, prueba de nuevo")
    num=int(input("Ingrese un número positivo: "))

print("El número es: ",num)
