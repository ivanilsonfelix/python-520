
nome = input("Digite seu nome:")

if len(nome) <=6:
    print("Nome invalido")
exit(0)
    print(
email=input("Digite seu email:")
CEP=input("Digite seu CEP:")

with open('cadastro.txt', 'a') as f:
    f.write("nome: %s / email: %s / CEP: %s\n" % (nome, email, CEP))

linha= input("Qual linha deseja visualizar?")

with open('cadastro.txt', 'r') as f:
    linhas = f.readlines()
    print(linhas[int(linha)])
