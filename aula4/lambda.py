var = lambda x,y: x*2*y

print(var(10, 3))


lista = [
	   lambda x: x** 2,
           lambda x: x** 3,
           lambda x: x** 4,
]

for a in anonimas:
    print(a(10))
