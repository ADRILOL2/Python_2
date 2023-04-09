def binario(b):
    return int(b,2)

def decimal(m):
    l=[]
    for e in m:
        l.append(binario(e))
    return l

a=["1111","1101","010011","11101011","11011"]
b=decimal(a)
for i,e in enumerate(b):
    print("el numero {} en binario es {}".format(e,a[i]))