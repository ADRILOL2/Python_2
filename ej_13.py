def lista(a):
    l=0
    for i in a:
        l+=1
    return l
e=input("escribe algo:\n")
print("Esta palabra tiene {} letras".format(lista(e)))