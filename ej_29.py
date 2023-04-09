def num_mayor(t,no):
    print("todos los numeros mayores que {} son:".format(no))
    for e in t:
        if no<e:
            print("{}".format(e))

def leer_tuple():
    a=[]
    i=0
    print("ahora, introduce los numeros que quieras, pulsa '-1' para salir")
    while i>-1:
        b=input("escribe cualquier numero:")
        a.append(b)
        if b=="-1":
            a.remove("-1")
            i-=1
            return a


a=input("escribe un numero:")
b=leer_tuple()
c=tuple(b)
num_mayor(c,a)