def superposición(x,y):
    n=0
    for e in x:
        n+= y.count(e)
    if n>0:
        return n
    else:
        return False

r=0
while r!=1:
    a=input("escribe una palabra:\n")
    b=input("escribe OTRA palabra:\n")
    c=superposición(a,b)
    if c!=0:
        print("Las palabras {} y {} tienen {} letras iguales\n".format(a,b,c))
    else:
        print("No tienen ningula letra igual\n")
    d=input("Continuar? s/n \n")
    if d=="s":
        print("Continuemos pues!")
    elif d=="n":
        print("Hasta luego!")
        r+=1
    else:
        print("Tomare eso como un no")
        r+=1