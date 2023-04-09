def leer_numero():
    return(int(input("introduce numero:")))

def leer_serie(a):
    s=0
    for i in range(a,1,-4):
        s+=i*2
    print("la suma de todos los numeros al cuadrado entre si a {} es {}".format(a,s))

q=leer_numero()
leer_serie(q)