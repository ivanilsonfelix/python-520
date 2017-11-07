lista=[1,2,3,4]
nova_lista = [item +1 for item in range(1,10,1) if item %2 == 0]

print(nova_lista)

nova_lista = []
for item in range (1,10,1):
    if item %2 ==0:
        nova_lista.append(item)
print(nova_lista)
