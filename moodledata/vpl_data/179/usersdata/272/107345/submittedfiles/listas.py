# -*- coding: utf-8 -*-

n=int(input('Digite o número de elementos: '))
a=[]
for i in range (0,n,1):
    a.append(int(input('Digite o valor: ')))

degrau=0
for j in range (0,len(a),1):
    if i==0:
        degrau=degrau+0
    else:
        dif=abs(a[j]-a[j-1])
