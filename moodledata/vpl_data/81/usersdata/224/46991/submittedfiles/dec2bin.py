# -*- coding: utf-8 -*-
p=int(input('Digite p:' ))
q=int(input('Digite q:' ))
cont=0
cont2=0
atual=q
while atual>0:
    atual=atual//10
    cont=cont+1
while q>0:
    valor=q%(10**cont)
    if valor==p:
        cont2=cont2+1   
    valor=q//(10**cont)
if cont!=0:
    print('S')
else:
    print('N')