def organizar():
    l=[0,0,0]
    l[0]=input("Nombre:")
    while l!=".":
        l[1]=int(input("año de nacimiento de {}:".format(l[0])))
        while l!=".":
            l[2]=2023-l[1]
            while l!=".":
                l.append
                return l

comenzar=input("hacer lista? s/n\n")
while comenzar=="s":
    a,b,c=organizar()
    print("""{:<20}{:<20}{:<20}
|{:<20}{:<20}{:<20}""".format("Nombre","Año de Nacimiento","Edad este año",a,b,c))