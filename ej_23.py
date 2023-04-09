def numero_menor(a):
    a.sort()
    return a[::1]

def numero_mayor(a):
    a.sort()
    return a[::-1]

l=[2,56,92,666,18,873,92]
c=numero_menor(l)
y=numero_mayor(l)
print("de los numeros '{}', {} es el mas pequeño y {} el mas grande".format(l,c[0],y[0]))