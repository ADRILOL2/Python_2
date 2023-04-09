def numero_mayor(x,y,z):
    if x>y:
        if x>z:
            return x
        else:
            return z
    elif y>z:
            return y
    else:
        return z

#formato principal
print("Bienvenid@ al codigo de 3 numero, este decidira cual es mayor,menor o igual de los 3 que pongas mas adelante")
a=int(input("\npon un numero:"))
b=int(input("\npon otro numero:"))
c=int(input("\nescribe otro numero numero:"))
d=numero_mayor(a,b,c)
print("el mas grande de {},{} y {} es: {}".format(a,b,c,d))