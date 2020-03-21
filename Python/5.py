def ebob(x,y):
	while y:
		r=x
		x=y
		y=r%y
	return x

def ekok(x,y):
	return x*y/ebob(x,y)

def eboblar(args):
    f, s, loop = args[0], args[1], args[2:]
    l = ebob(f, s)
    for i in loop:
        l = ebob(l, i)
    return l

def ekoklar(args):
    f, s, loop = args[0], args[1], args[2:]
    l = ekok(f, s)
    for i in loop:
        l = ekok(l, i)
    return l


print(int(ekoklar([i for i in range(1, 21)])))
