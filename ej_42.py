def leer_numero():
    return(int(input("Escribe un numero:")))

def tabla_suma(a,b):
    print("tabla de suma de pares de {}".format(a))
    p=0
    for i in range(b+1):
        c=i+a
        if c%2==0:
            p+=1
            print("{} + {} = {}".format(i,a,c))

    print("la cantidad de numeros pares son {}".format(p))

a=leer_numero()
b=int(input("escribe hasta donde quieres sumar: "))
tabla_suma(a,b)