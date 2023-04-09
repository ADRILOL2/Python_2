def repetidos(x,y):
    a=y*int(x)
    return a

o=0
while o!=1:
    n=input("escribe un a palabra:")
    r=input("escribe la cantidad exacta que quieres que se repita '{}'\n".format(n))
    e=repetidos(r,n)
    print("la palabra {} repetida {} vezes es:\n{}".format(n,r,e))
    d=input("Continuar? s/n \n")
    if d=="s":
        print("ta bien")
    elif d=="n":
        print("Hasta luego!")
        o+=1
    else:
        print("Tomare eso como un no")
        o+=1