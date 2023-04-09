def crear_lista(a,b):
    l=[]
    if a<b:
        for e in range(a,b+1,1):
            l.append(e)
    elif b<a:
        for e in range(b,a+1,1):
            l.append(e)
    else:
        l.append(a)
    return l

def sumar_lista(s):
    suma = 0
    for i in s:
        suma+=i
    return suma

n=int(input("escribe un numero:"))
nn=int(input("Escribe otro numero:"))
x=crear_lista(n,nn)
e=sumar_lista(x)
print("la sumade los numeros entre {} y {} es:{}".format(n,nn,e))
