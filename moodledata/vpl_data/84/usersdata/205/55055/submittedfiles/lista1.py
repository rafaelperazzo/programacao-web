# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de elementos da lista:'))
a=[]
qpar=0
qimpar=0
spar=0
simpar=0
for i in range (1,n+1,1):
    valor=int(input('digite o valor da lista:'))
    a.append(valor)
for j in range (0, len(a),1):
    if (a[j]%2==0):
        qpar=qpar+1
        spar=spar+a[j]
    else:
        qimpar=qimpar+1
        simpar=simpar+a[j]
print(simpar)
print(spar)
print(qpar)
print(qimpar)
print(a)
        
        

