def leer_lista():
	a=[]
	c="a"
	while c!=".":
	    c=input("Introdueixi un element de la llista i punt (.) per acabar: ")
	    if c!=".":
        	a.append(c)
	return a

def orden(a):
	b=a.copy()
	a.sort()
	if a==b:
		print("la lista {} esta en orden".format(b))
	else:
		print("la lista {} NO esta en orden".format(b))

a=leer_lista()
orden(a)