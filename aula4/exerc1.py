alunos = [

]

menu = """
[MENU]

1) Inserir
2) Mostrar
3) Sair
Insira uma opção: """


def inserir_aluno():
    nome = input("Insira o nome: ")
    email = input("Insira o email: ")

    alunos.append({
        "nome": nome,
        "email": email
    })

def mostrar_aluno():
    global alunos
    aluno = input("Informe o nome do aluno: ")
    for a in alunos:
        if a['nome'] == aluno:
            return(a['email'])
while True:
    opcao = int(input(menu))

    if opcao ==1:
        inserir_aluno()
    elif opcao ==2:
        print(mostrar_aluno())
    elif opcao ==3:
        break
    else:
	    print("nenhuma opcao valida")
