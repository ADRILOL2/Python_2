

def leer_palabras():
    return(input("Escribe una palabra:"))

def comparar(a,b):
    if a==b:
        print("son lo mismo")

    elif a[-3:]==b[-3:]:
        print("Riman B)")

    elif a[-2:]==b[-2:]:
        print("Riman un poco")

    elif a[-1:]==b[-1:]:
        print("Riman por muy poco")

    else:
        print("No riman carahuevo")

a=leer_palabras()
b=leer_palabras()
comparar(a,b)