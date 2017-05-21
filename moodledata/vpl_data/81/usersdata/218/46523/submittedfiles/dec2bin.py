# -*- coding: utf-8 -*-
p=int(input('digite o valor de p:'))
q=int(input('digite o valor de q:'))
temp=p
i=0
while temp>0:
    temp=temp//10
    i=i+1
cont=0
while q>0:
    resto=q%(10**i)
    if resto==p:
        cont=cont+1
    q=q//10
if cont!=0:
    print('sim')
else:
    print('não')