# -*- coding: utf-8 -*-
p=int(input('Digite p:'))
q=int(input('Digite q:'))

cont=1
temp=p
while temp>0:
    cont=cont+1
    temp=temp//10
    
cont2=0
while temp<0:
    n=q%(10**cont)
    if n==p:
        cont2=cont2+1
        q=q//10
        
print('n')

