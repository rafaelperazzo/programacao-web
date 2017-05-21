# -*- coding: utf-8 -*-
p=int(input('digite o valor do menor número:'))
q=int(input('digite o valor do maior número:'))
n=p
el=0
while (n%10)>0:
    el=el+1
    n=n//10
cont=0
i=el
while (q//(10**el))>0:
   teste=q%(10**el)
   if teste==p:
        cont=cont+1
if cont!=0:
    print('S')
else:
    print('N')
