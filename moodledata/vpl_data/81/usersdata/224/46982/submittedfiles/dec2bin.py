# -*- coding: utf-8 -*-
p=int(input('Digite p:' ))
q=int(input('Digite q:' ))
cont=0
atual=q
while atual>0:
    atual=atual//10
    cont=cont+1
print(cont)
