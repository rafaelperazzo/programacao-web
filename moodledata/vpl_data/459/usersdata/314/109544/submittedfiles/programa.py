# -*- coding: utf-8 -*-
lista=[]
cont=0
nconsultas=int(input('Digite o numero de visitas: '))
for i in range(nconsultas):
        comprimento=int(input('Digite os comprimentos dos tacos: ')))
        if comprimento not in lista:
            lista.append(comprimento)
            cont+=2
        else:
            lista.remove(comprimento)

print(cont)            