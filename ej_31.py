def contar_vocales():
    b=("a","e","i","o","u","otros")
    vocales=[0,0,0,0,0,0]
    for i,e in enumerate():
        if e=="a" or e=="A" or e=="á" or e=="Á":
            vocales[0]+=1
        elif e=="e" or e=="E" or e=="é" or e=="É":
            vocales[1]+=1
        elif e=="i" or e=="I" or e=="í" or e=="Í":
            vocales[2]+=1
        elif e=="o" or e=="O" or e=="ó" or e=="Ó":
            vocales[3]+=1
        elif e=="u" or e=="U" or e=="ú" or e=="Ú":
            vocales[4]+=1
        else:
            vocales[5]+=1
            for i,e in enumerate(vocales):
                print("la vocal {} se repite {} vezes".format(b[i],vocales[i]))

p=input("escribe una palabra:")
contar_vocales(p)
