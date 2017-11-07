alunos = [

	{
	    "nome":"Gabriel",
	    "notas":["1","4","5","6"]
	}
	{
	    "nome":"Joao",
	    "notas": ["3","5", "7","7"]
	}
]    

nome = input ("Qual o nome do aluno:")


for a in alunos:
    if a["nome"] == nome:
		total = 0
      for n in a["notas"]:
		total += n
		media = total / len(a["notas"])
		if media >= 7:
		print("aprovado")
		else:
		print("reprovado")
       
# ==========
      

for a in alunos:
    if a["nome"] == nome:
	print("a" if sum(a["notas"])/len(a["notas"]) >= 7 else "r")
     
      


    		


