# -*- coding: utf-8 -*-
p=int(input('Digite P:'))
q=int(input('Digite Q:'))
cont=0
temp=p
cont2=0
while temp>0:
    temp=temp//10
    cont=cont+1
    
while q>0:
    n=q%(10**cont)
    if n==p:
        cont2=cont2+1
    q=q//10
    
if cont2>0:
    print('S')
else:
    print('N')
    

