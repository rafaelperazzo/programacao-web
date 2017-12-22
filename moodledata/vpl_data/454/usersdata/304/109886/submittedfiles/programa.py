# -*- coding: utf-8 -*-
c = int(input('Digite o número de consultas ao estoque: '))
pedidos = []
fabricados = []
for i in range (0,c,1):
    pedidos.append(int(input('Digite a consulta: ')))
for i in range (0,c,1):
    if pedidos[i] not in fabricados:
        fabricados.append(pedidos[i])
        fabricados.append(pedidos[i])
print (len(fabricados))

