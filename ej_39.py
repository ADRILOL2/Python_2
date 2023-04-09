
import time
n=int(input("escribe un numero:"))
r=int(input("escribe la cantidad que quieres que se renumere {}:".format(n)))
for i in range(r):
    for j in range(n):
        print("nivel {}, numero {}".format(i+1,j+1))
        time.sleep(1)