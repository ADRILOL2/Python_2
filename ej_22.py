def forma(a):
        if a==1:
            print("""
. . . . .
.       .
.       .
.       .
. . . . .""")
        elif a==2:
            print("""
    . . . . . . . . .
    .               .
    .               .
    .               .
    . . . . . . . . .""")
        elif a==3:
            print("""
        .
       . .
      .   .
     .     .
    . . . . .""")
        else:
            print("Elije una de las formas que hay en el menu")

def menu():
    print("""
                [MENU]
    1. Cuadrado
    2. Rectangulo
    3. Triangulo
    4. Salir\n""")
    e=int(input("¿que numero elijes? \n"))
    return e
l=0
while l!=1:
    i=menu()
    if i==4:
        print("Chau!")
        l+=1
    else:
        f=forma(i)
