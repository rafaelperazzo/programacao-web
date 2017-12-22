# -*- coding: utf-8 -*-

n=int(input('Digite o número de elementos: '))
a=[]
for i in range (0,n,1):
    a.append(int(input('Digite o valor: ')))

degrau=0
for j in range (1,len(a)+1,1):
    valor=abs(a[j]-a[j-1])
    if (valor>degrau):
        degrau=valor
    else:
        degrau=degrau+0
print(degrau)
