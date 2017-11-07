import MySQLdb

try:
    con = MySQLdb.connect(
        host="localhost",
        user="admin",
        passwd="4linux--",
        db="projetos"
    )
    cur = con.cursor()

    ### INSERT
    cur.execute("INSERT INTO clientes(nome,endereco) \
                 VALUES('mariana', 'mariana@4linux.com.br')"
    )

    ### UPDATE
    cur.execute("UPDATE clientes SET endereco='gabriel@gabriel' \
                WHERE nome='gabriel'")

    ## DELETE
    # cur.execute("DELETE FROM alunos WHERE nome='mariana'")

    con.commit()
except Exception as e:
    con.rollback()
    cur.close()
    con.close()


### SELECT

try:

    con = MySQLdb.connect(
        host="localhost",
        user="admin",
        passwd="4linux--",
        db="projetos"
    )

    cur = con.cursor()

    ### SELECIONA MAIS DE UM
    cur.execute("SELECT * FROM clientes")
    registros = cur.fetchall()

    print(registros)

    ### SELECIONA APENA UM
    cur.execute("SELECT * FROM clientes WHERE nome='mariana'")
    registro = cur.fetchone()

    print(registro)

except Exception as e:
    print(e)
    con.rollback()
    cur.close()
    con.close()

### MOSTRA TODOS ENCONTRADOS
for r in registros:
    print('Id: ', r[0])
    print('Nome: ', r[1])
    print('Email: ', r[2])

### MOSTRA APENAS O PRIMEIRO
print('Id: ', registro[0])
print('Nome: ', registro[1])
print('Email: ', registro[2])
    






