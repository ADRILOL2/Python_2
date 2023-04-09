def todos():
    b=[]
    for i in range (0,100):
        b.append(i)
    print(b)

def impares():
    b=[]
    for i in range (0,100):
        if i%2==1:
            b.append(i)
    print(b)


def pares():
    b=[]
    for i in range (0,101):
        if i%2==0:
            b.append(i)
    print(b)

n=0
while n!=1:
    e=input("""\nOpción de 0 al 100:
1.todos los numeros
2.solo impares
3.solo pares
4.salir
¿Cual elijes?
""")
    if e=="1":
        todos()
    elif e=="2":
        impares()
    elif e=="3":
        pares()
    elif e=="4":
        n+=1
    else:
        print("ERROR !!")