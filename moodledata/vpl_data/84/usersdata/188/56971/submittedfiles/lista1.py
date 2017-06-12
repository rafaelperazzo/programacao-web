# -*- coding: utf-8 -*-
n=int(input('Digite o número de elementos da lista:'))
icarus=[]
i=0
for i in range (1,n,1):
    valor=int(input('Digite o elemento:'))
    icarus.append(valor)
contp=0
conti=0
somap=0
somai=0
for i in range(0,len(icarus),1):
    if icarus[i]%2==0:
        contp=contp+1
        somap=somap+(icarus[i])
    else:
        conti=conti+1
        somai=somai+(icarus[i])
print(somai)
print(somap)
print(conti)
print(contp)
print(icarus)