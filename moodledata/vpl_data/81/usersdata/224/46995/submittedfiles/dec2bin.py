# -*- coding: utf-8 -*-
p=int(input('Digite p:' ))
q=int(input('Digite q:' ))
i=0
cont=0
atual=q
while atual>0:
    atual=atual//10
    i=i+1
while q>0:
    valor=q%(10**i)
    if valor==p:
        cont=cont+1   
    q=q//10
if cont!=0:
    print('S')
else:
    print('N')