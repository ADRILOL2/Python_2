def pares(a,s):
    ll=[]
    for i in range(s+1):
        if a%2==0:
            ll.append(a)
    return ll
sn=0
l=[]
e="r"
while e!=".":
    e=input("escribe un numero, pulsa '.' para parar:")
    if l[:-1]==".":
        l.remove (".")
    else:
        l.append(e)
        sn+=1
p=pares(l,sn)
print("de la lista de numeros {} nos quedamos con:\n{}".format(l,p))