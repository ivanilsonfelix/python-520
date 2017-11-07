maior = 0
dicio = {
	1: "primeiro",
	2: "segundo",
	3: "terceiro"
}
	

for i in range(1,4,1):
    num = int (input("Digite o %s numero:" % dicio[i]))
    if num>maior:
    maior=num
print( "o maior numero e: %s" %maior)

