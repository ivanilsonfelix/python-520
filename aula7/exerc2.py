import psycopg2

class Banco:

    cur = None
    con = None

    def __init__(self):
        self.con = psycopg2.connect(
            "host=localhost \
             dbname=projeto \
             user=admin \
             password=4linux"
        )

        self.cur = self.con.cursor()

    def inserir(self, tabela, dados):

        keys = []
        values = []

        for key, value in dados.items():
            keys.append(key)
            values.append("'%s'" % value)

        campos = ','.join(keys)
        valores = ','.join(values)

        self.cur.execute(
            "INSERT INTO %s(%s) VALUES(%s)"
            % (tabela, campos, valores)
        )
        self.con.commit()

    def alterar(self, tabela, dados, condicao):

        setlist = []

        for key, value in dados.items():
            setlist.append("%s='%s'" % (key, value))

        set = ', '.join(setlist)

        query = "UPDATE %s SET %s WHERE %s" % (tabela, set, condicao)

        self.cur.execute(query)
        self.con.commit()

    def remover(self, tabela, condicao):

        query = "DELETE FROM %s WHERE %s" % (tabela, condicao)

        self.cur.execute(query)
        self.con.commit()

    def buscar_um(self, tabela, condicao):
        query = "SELECT * FROM %s WHERE %s" % (tabela, condicao)

        self.cur.execute(query)

        return self.cur.fetchone()

    def buscar_todos(self, tabela):
        query = "SELECT * FROM %s" % (tabela)

        self.cur.execute(query)

        return self.cur.fetchall()


banco = Banco()

dados = {
    "nome": "Mariana",
    "email": "mariana@4linux.com.br"
}

banco.inserir(tabela='alunos', dados=dados)

todos = banco.buscar_todos(tabela='alunos')
print(todos)

