# -*- coding: utf-8 -*-
c=int(input('Digite o numero de consultas: '))
ped=[]
fab=[]
for i in range(0,c,1):
    pedidos.append(int(input('Digite o tamanho do taco: ')))
for i in range(0,c,1):
    if ped[i] not in fab:
        fab.append(ped[i])
        fab.append(ped[i])
print(len(fab))

