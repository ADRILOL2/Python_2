def leer_numero():
    return(int(input("introduce valor:")))

def leer_float():
    return(float(input("introduce valor real:")))

def calcular(x,y,z):
    return(x*(1+y/100)**z)

q=leer_numero()
i=leer_float()
a=leer_numero()
c=calcular(q,i,a)
print("solicitas {} a un interes anual de {} con {} años, pagaras {} euros".format(q,i,a,c))