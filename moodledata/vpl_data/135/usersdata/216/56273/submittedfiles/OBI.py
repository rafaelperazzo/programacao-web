# -*- coding: utf-8 -*-
n=int(input('Digite o volume:'))
t=int(input('Digite o numero de trocas:'))
i=0
soma=n
a=[]

for i in range(1,t+1,1):
    b=int(input('Digite a quantidade de vezes do botão:'))
    a.append(b)
    
for i in range(0,len(a),1):
    soma=soma+a[i]
    if soma>100:
        soma=100
    elif soma<0:
        soma=0
print(soma)