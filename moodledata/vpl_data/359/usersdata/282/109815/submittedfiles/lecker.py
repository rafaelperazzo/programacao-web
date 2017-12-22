# -*- coding: utf-8 -*-
c=int(input('Digite o número de consultas: '))
pedidos=[]
fabricados=[]
for i in range (0,c,1):
    pedidos.append(int(input('Digite o tamanho do taco: ')))
for i in range(0,c,1):
    if pedidos[1] not in fabricados:
        fabricados.append(pedidos[i])
        fabricados.append(pedidos[i])
print(len(fabricados))

