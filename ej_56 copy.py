def escalera(x):
    l=[]
    for e in range(x,0,-1):
        l.append(e)
    print(' '.join(map(str,l)))
n=int(input("pon un numero:"))
while n!=0:
    for i in range(n,0,-1):
        escalera(n)
        n-=1

#ej_31.py