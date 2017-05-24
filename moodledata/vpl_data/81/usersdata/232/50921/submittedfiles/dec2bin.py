# -*- coding: utf-8 -*-
p=int(input('Digite o valor de p: '))
q=int(input('Digite o valor de q: '))
x=str(p)
i=len(x)
cont=0

while q>0:
    resto=q%(10**i)
    if resto==p:
        cont=cont+1
    q=q//10
if cont!=0:
    print('S')
else:
    print('N')
    

