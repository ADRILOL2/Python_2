def escrito(s):
    mayus=sum(c.isupper()for c in s)
    minus=sum(c.islower()for c in s)
    num=sum(c.isdigit()for c in s)
    espec=len(s)-(mayus+minus+num)
    return mayus,minus,num,espec


p=input("escribe una cadena\n")
ma,mi,n,e=escrito(p)
print("""lo que escribiste '{}' tiene:
{} mayusculas
{} minusculas
{} numeros y
{} caracteres especiales.""".format(p,ma,mi,n,e))