# -*- coding: utf-8 -*-

qp=int(input('Digite a quantidade de portas:'))
pe=int(input('Digite a porta de entrada:'))
ps=int(input('Digite a porta de saída:'))
x=[]

for i in range(0, qp , 1):
    v=int(input('Digite a vida:'))
    x.append(v)
soma=0
for i in range(pe, ps+1, 1):
    soma=soma+x[i]
print(soma)

