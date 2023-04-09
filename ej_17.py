def invertir(a):
	b = list(a)
	c = b[::-1]
	r = "".join(c)
	return r

def palindromo(a):
	e = invertir(a)
	x=0
	for i in range(len(a)):
		if a[i]!=e[i]:
			x+=1
		if x==0:
			return True
		else:
			return False


e=0
while e!=1:
	s=input("\nescribe algo aqui que se lea igual de los 2 lados, automaticamente se escribira alreves mientras no escribas '.'\n")
	if palindromo(s):
		print("la palabra {} es un palindromo".format(s))
	else:
		print("la palabra {} NO es un palindromo".format(s))
	r=input("Quieres seguir? s/n\n")
	if r=="s":
		print("Continuemos pues :D\n")
	elif s==".":
		e+=1
	else:
		e+=1