alunos = [{"nome":"Mariana", "cursos":["Python"]},{"nome":"Joao","cursos": ["Python", "Infra Agil"]}]

curso = input ("digite o nome do curso:")

for a in alunos:
     for c in a["cursos"]:
         if c == curso:
           print(a["nome"])
