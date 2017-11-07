from pymongo import MongoClient

client = MongoClient('localhost')
db = client['dexterops']

menu = """
1) INSERIR
2) MOSTRAR
4) SAIR
"""

while True:

    opcao = int(input(menu))

    if opcao == 1:
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")

        aluno = {"nome": nome, "email": email}
        if db.alunos.insert(aluno):
            print('Inserido com sucesso')
        else:
            print('Falha ao inserir')
    elif opcao == 2:
        email = input("Digite o email: ")
        aluno = db.alunos.find({"email": email})

        for a in aluno:
            print(a['nome'])
    elif opcao == 3:
        email = input("Digite o email: ")

        if db.alunos.remove({"email": email}):
            print("Registro removido")
        else:
            print("Falha ao remover")
    elif opcao == 4:
        email = input("Digite o email: ")

        novo_nome = input("Digite o nome: ")
        novo_email = input("Digite o email: ")

        dados = {
            "$set": {"nome": novo_nome, "email": novo_email}
        }

        result = db.fila.update({"email": email}, dados)

        if result['updatedExisting']:
            print("Registro alterado com sucesso!")
        else:
            print("Falha ao alterar")

    elif opcao == 4:
        exit(0)

