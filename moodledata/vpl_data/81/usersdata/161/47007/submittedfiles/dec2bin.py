# -*- coding: utf-8 -*-
p=int(input('Digite o valor de p:'))
q=int(input('Digite o valor de q:'))
i=0
contador=0
x=p
while x>0:
    x=x//10
    i=i+1
while q>0:
    resto=q%(10**i)
    if resto==p:
        contador=contador+1
    q=q//10    
if contador!=0:
    print('S')
else:
    print('N')