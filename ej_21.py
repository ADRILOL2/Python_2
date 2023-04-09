def repetidos(x,y):
    a=y*int(x)
    return a
def puntos(x):
    for e in x:
        c=repetidos(int(e),".")
    return c

o=0
while o!=1:
    n=input("escribe una cantidad de '.':")
    e=puntos(n)
    print("la lista de '.' repetida {} vezes es:\n{}".format(n,e))
    d=input("Continuar? s/n \n")
    if d=="s":
        print("ta bien")
    elif d=="n":
        print("Hasta luego!")
        o+=1
    else:
        print("Tomare eso como un no")
        o+=1