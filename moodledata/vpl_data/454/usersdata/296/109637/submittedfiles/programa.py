# -*- coding: utf-8 -*-
C = int(input("Digite o número de consultas ao estoque: "))
pedidos = []
fabricados = []
for i in range (0,C,1):
    pedidos.append(int(input("Digite o comprimento do taco: ")))
for i in range (0,C,1):
    if pedidos[i] not in fabricados:
        fabricados.append(pedidos[i])
        fabricados.append(pedidos[i])
print(len(fabricados))


