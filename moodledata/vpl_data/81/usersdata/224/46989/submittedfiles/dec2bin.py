# -*- coding: utf-8 -*-
p=int(input('Digite p:' ))
q=int(input('Digite q:' ))
cont=0
cont2=0
atual=q
u=p
while atual>0:
    atual=atual//10
    cont=cont+1
    g=cont
while u>0:
    u=u//10
    cont2=cont2+1
    h=cont2
    valor=q/(g-h)
while valor>0:
    valor=q%(g-h)
    if valor==p:
        print('S')
    valor=q//(g-h)
    else:
        print('N')