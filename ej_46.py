import random
def elementos():
    l=[]
    for l in range(20):
            l.append(random.randint(1,100))
    return l

def copiados(a):
        seen = set()    
        dupes = [x for x in a if x in seen or seen.add(x)] 	 
        if len(dupes)>0:
              print("La llista {} té elements duplicats {}".format(a,dupes))
        else:
              print("La llista {} no té elements duplicats {}".format(a,dupes))
        
def elimina_duplicats(a):
    b= list(set(a))
    return b


def eliminar_copiados(a):
      b=list(set(a))
      return b

x=elementos
copiados(x)
y=eliminar_copiados(x)
y.sort()
print("""la lista seria tal que asi:
{}""".format(y))