def numero_mayor(x,y):
    if x>y:
        print("{} es major que {}".format(x,y))
    elif x<y:
        print("{} es menor que {}".format(x,y))
    else:
        print("{} es igual que {}".format(x,y))
#formato principal
a=int(input("pon un numero:"))
b=int(input("pon otro numero:"))
numero_mayor(a,b)