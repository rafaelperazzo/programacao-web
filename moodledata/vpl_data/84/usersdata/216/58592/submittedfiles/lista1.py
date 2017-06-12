# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade:'))
v=[]
somaimpares=0
somapares=0
contimpares=0
contpares=0

for i in range(0,n,1):
    a=int(input('Digite um valor:'))
    v.append(a)

for i in range(0,len(v),1):
    if v[i]%2==1:
        somaimpares=somaimpares+v[i]
        contimpares=contimpares+1
    if v[i]%2==0:
        somapares=somapares+v[i]
        contpares=contpares+1
print(somaimpares)
print(somapares)
print(contimpares)
print(contpares)
print(v)

