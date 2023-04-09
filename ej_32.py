def año(a):
    if a%4==0 and (a%100==0 or a%400>0):
        print("es un año de transpaso") 
    else:
        print("{} No es un año de transpaso".format(a))

n=input("escribe un año:")
año(int(n))