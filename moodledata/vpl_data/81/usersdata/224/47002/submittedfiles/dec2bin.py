# -*- coding: utf-8 -*-
p=int(input('Digite p:' ))
q=int(input('Digite q:' ))
i=0
c=0
v=p
cont=0
atual=q
while atual>0:
    atual=atual//10
    i=i+1
while v>0:
    v=v//10
    c=c+1
while q>0:
    valor=q%(10**(i-c))
    if valor==p:
        cont=cont+1   
    q=q//10
if cont!=0:
    print('S')
else:
    print('N')