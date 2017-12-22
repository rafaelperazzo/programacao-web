# -*- coding: utf-8 -*-
n=int(input("Digite o numero de consultas: "))
pedidos=[]
fabricados=[]
for i in range (0,n,1):
    pedidos.append (int(input("Digite um tamanho: ")))
    
for i in range(0,n,1):
    if pedidos[i] not in fabricados:
        fabricados.append(pedidos[i])
        fabricados.append(pedidos[i])
print (len(fabricados))
