def num_mayor(i,n):
    l=[]
    print("todos los nombres que comienzan con '{}' son:".format(i))
    for e in n:
        if e(0)==i:
            l.append(e)
    print("{}".format(l))

def leer_tuple():
    a=[]
    i=0
    print("ahora, introduce los nombres que quieras, pulsa '1' para salir")
    while i>-1:
        b=input("escribe cualquier nombre:")
        a.append(b)
        if b=="1":
            a.remove("1")
            i-=1
            return a

i=input("escribe una inicial:")
b=leer_tuple()
c=num_mayor(i,b)
