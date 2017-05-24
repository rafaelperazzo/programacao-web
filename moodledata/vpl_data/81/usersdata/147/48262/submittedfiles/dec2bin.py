# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
i=0
cont=0
temp=p
while temp>0:
    temp=temp//10
    i=i+1
    while q>0:
        resto=q%(10**i)
        if resto==p:
            cont=cont+1
        q=q//10
        i=i+1
if cont!=0:
    print('subnumero')
else:
    print('nao é sub')
    
    

