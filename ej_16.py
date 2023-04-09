def invertir(a):
	b = list(a)
	c = b[::-1]
	r = "".join(c)
	return r
# Programa principal
e=0
while e!=1:
	s=input("\nescribe algo aqui, automaticamente se escribira alreves mientras no escribas '.'\n")
	if s!=".":
		print("{} al reves és {}".format(s,invertir(s)))
	else:
		e+=1