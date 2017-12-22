# -*- coding: utf-8 -*-
a=int(input("Digite o numero de consultas: "))
pedidos=[]
fabricados=[]
for i in range (0,n,1):
    pedidos.append (int(input("Digite umtamanho: ")))
    if pedidos[i] not in fabricados:
        fabricados.append(pedidos[i])
        fabricados.append(pedidos[i])
print (len(fabricados))
