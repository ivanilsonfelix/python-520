
import psycopg2

menu = """
[MENU]

1) Inserir
2) Alterar
3) Deletar
4) Sair
Insira uma opção: """

con = psycopg2.connect(
    "host=localhost \
     dbname=projeto \
     user=admin \
     password=4linux"
)

cur = con.cursor()

while True:
    opcao = int(input(menu))

    if opcao == 1:
        nome = input('Insira o nome: ')
        email= input('Insira o email: ')
        try:
            cur.execute(
                "INSERT INTO alunos(nome, email) VALUES('%s', '%s')"
            )
            print('Registro inserir com sucesso')
        except Exception as e:
            print('Falha ao inserir')
            print(e)
    elif opcao == 2:

        aluno = input('Qual aluno deseja alterar?: ')

        nome = input('Insira o nome: ')
        email = input('Insira o email: ')

        try:
            cur.execute(
                "UPDATE alunos SET nome='%s', email='%s' \
                WHERE aluno='%s'" % (nome, email, aluno)
            )
            print('Registro alterado com sucesso')
        except Exception as e:
            print('Falha ao alterar')
    elif opcao == 3:
        aluno = input('Qual aluno deseja remover?: ')

        nome = input('Insira o nome: ')

        try:
            cur.execute(
                "DELETE FROM alunos WHERE aluno='%s'" % aluno
            )
            print('Registro removido com sucesso')
        except Exception as e:
            print('Falha ao remover')

    elif opcao == 4:
        break
        try:
            cur.execute(
                "UPDATE alunos SET nome='%s', email='%s' \
                WHERE aluno='%s'" % (nome, email, aluno)
            )
            print('Registro alterado com sucesso')
        except Exception as e:
            print('Falha ao alterar')
    elif opcao == 3:
        aluno = input('Qual aluno deseja remover?: ')

        nome = input('Insira o nome: ')

        try:
            cur.execute(
                "DELETE FROM alunos WHERE aluno='%s'" % aluno
            )
            print('Registro removido com sucesso')
        except Exception as e:
            print('Falha ao remover')

    elif opcao == 4:
        break
while True:
    opcao = int(input(menu))
    
    if opcao == 1:
        nome = input('Insira o nome: ')
        email= input('Insira o email: ')
        try:
            cur.execute(
                "INSERT INTO alunos(nome, email) VALUES('%s', '%s')"
            )
            print('Registro inserir com sucesso')
        except Exception as e:
            print('Falha ao inserir')
            print(e)
    elif opcao == 2:
        aluno = input('Qual campo deseja alterar?:')
        nome = input('Insina o nome:')
        email = input('Insira o email:')
        try:
            cur.execute("UPDATE alunos SET nome='%s', email='%s' \
                WHERE alunos='%s'" % (nome, email, aluno))
            print('Registro alterado com sucesso')
        except Exception as e:
            print('Falha ao alterar')
    elif opcao ==3:
        aluno= input('Qual o campo deseja deletar?:')
        nome = input('Insira o nome: ')
    
        try:
            cur.execute("DELETE FROM alunos WHERE nome='%s'", email='%s'" \
                % (nome, email, aluno))
            print('Deletado com sucesso')
        except Exception as e:
            print('Falha ao deletar')
       
    elif opcao == 4:
        break

