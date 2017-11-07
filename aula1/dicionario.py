
x={
    "curso": "pythun",
    "escola": "4linux",
    "aluno": [
        "Leonardo",
        "Gabriel",
        "Colla",
        [
            "gabriel.bonfim@4linux.com.br"
        ] 
    ], 
    "notas": {
        "b1":10,
        "b2":9,
        "b3":4, 
        "b4":7,
     }
}
print(type(x))
print(x.values())
x["notas"]["b3"] = 7
print(x["notas"])

print(x["aluno"][1])

