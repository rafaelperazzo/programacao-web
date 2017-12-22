# -*- coding: utf-8 -*-
c=int(input('insira o número de consultas: '))
pedidos=[]
fabricados=[]
for i in range(0,c,1):
    pedidos.append(int(input('digite o comprimento do taco: ')))
for i in range(0,c,1):
    if pedidos[i] in estoque:
        for j in range(0,len(estoque),1):
            if pedidos[i] == estoque[j]:
                del estoque[j]
                break
    else:
        fabricados.append(pedidos[i])
        fabricados.append(pedidos[i])
        estoque.append(pedidos[i])
print(len(fabricados))        