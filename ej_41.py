def leer_numero():
    return(int(input("Escribe un numero:")))

def tabla_suma(a,b):
    print("tabla de multiplicar de {}".format(a))
    for i in range(b+1):
        c=i+a
        print("{} + {} = {}".format(i,a,c))
        if c%2==0:
            print("es par")
        else:
            print("es inpar")

a=leer_numero()
b=int(input("escribe hasta donde quieres sumar: "))
tabla_suma(a,b)