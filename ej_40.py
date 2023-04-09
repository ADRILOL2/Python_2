def leer_numero():
    return(int(input("Escribe un numero:")))

def tabla_multiplicadora(a,b):
    print("tabla de multiplicar de {}".format(a))
    for i in range(b+1):
        print("{} x {} = {}".format(i,a,i*a))

a=leer_numero()
b=int(input("escribe hasta donde quieres multiplicar: "))
tabla_multiplicadora(a,b)
