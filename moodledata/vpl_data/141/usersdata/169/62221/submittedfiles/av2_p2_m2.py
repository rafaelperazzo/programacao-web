# -*- coding: utf-8 -*-
qs=int(input('Digite a Quantidade de Salas:'))
pe=int(input('Digite a Porta de Entrada:'))
ps=int(input('Digite a Porta de Saída:'))
l1=[]
for i in range(0,qs,1):
    v=float(input('Digite o Quantidade de Vidas de Cada Sala:'))
    l1.append(v)
soma=0
for i in range(pe,ps+1,1):
    soma=soma+l1[i]
print(soma)
    

