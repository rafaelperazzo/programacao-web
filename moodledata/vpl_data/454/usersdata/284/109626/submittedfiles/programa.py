c=(int(input('digite o numero de consultas: ')))
pedidos=[]
fabricados=[]
for i in range(0,c,1):
    pedidos.append(int(input('digite o numero do taco: ')))
for i in range(0,c,1):
    if pedidos[i] not in fabricados:
        fabricados.append(pedidos[i])
        fabricados.append(pedidos[i])
print(len(fabricados))

