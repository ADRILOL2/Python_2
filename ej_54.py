def pares(l):
    ll=[]
    for i,e in enumerate(l):
        if i%2==0:
            ll.append(e)
    return ll

l=[]
e="r"
while e!=".":
    e=input("escribe un numero, pulsa '.' para parar:")
    if l[:-1]==".":
        l.remove (".")
    else:
        l.append(e)
p=pares(l)
print("de la lista de numeros {} nos quedamos con:\n{}".format(l,p))