from pymongo import MongoClient

## CONEXAO
client = MongoClient('localhost')
db = client['dexterops']

## INSERT
fila = {"servico": "Intranet", "status": 0}
id = db.fila.insert(fila)

## DELETE
# db.fila.remove({"_id": id})

## BUSCAR TODOS
items = db.fila.find()
for i in items:
    print(i['_id'])

## BUSCAR UM
item = db.fila.find({"_id": id})
for i in item:
    print(i)

## UPDATE
dados = {
    "$set": {"status": 1}
}

result = db.fila.update({"_id": id}, dados)

print(result)

if result['updatedExisting']:
    print("Registro alterado com sucesso!")
