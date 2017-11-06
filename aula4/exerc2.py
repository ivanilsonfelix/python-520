alunos = [

]

banco = [
    {
        "login": "gabriel",
        "senha": "123456"
    }
]

logado = False


menu = """
[MENU]

1) Login
2) Inserir
3) Mostrar
4) Sair
Insira uma opção: """

def is_logged(*args):
    def func():
        if logado:
            return args[0]()
        else
            return print('Ṕermissao negada')
    return func

@is_logged 
def inserir_aluno():
    global alunos, logado

    if not logado:
        print("Acesso negado")
        return

    nome = input("Insira o nome: ")
    email = input("Insira o email: ")

    alunos.append(
        {
            "nome": nome,
            "email": email
        }
    )

def mostrar_aluno():
    global alunos, logado

    if not logado:
        print("Acesso negado")
        return

    aluno = input("Informe o nome do aluno: ")
    for a in alunos:
        if a['nome'] == aluno:
            return a['email']

def login():
    global logado, banco

    login = input("Insira o login:")
    senha = input("Insira a senha:")

    for b in banco:
        if login == b["login"] and senha == b["senha"]:
            logado = True
            return True
        else:
            return False



while True:
    opcao = int(input(menu))

    if opcao == 1:
        if login():
            print("Login realizado com sucesso!")
        else:
            print("Usuario e/ou senha invalido")
    elif opcao == 2:
        inserir_aluno()
    elif opcao == 3:
        print(mostrar_aluno())
    elif opcao == 4:
        break
    else:
        print("Nenhuma opção válida")

