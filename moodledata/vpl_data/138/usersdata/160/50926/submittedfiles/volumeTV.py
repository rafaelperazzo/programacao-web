# -*- coding: utf-8 -*-
 
v=int(input('Digite o volume inicial:'))
t=int(input('Digite as alterações feita no volume:'))
i=0
cont=v
for i in range(1,t+1,1):
    a=int(input('Digite a alteração feita no volume:'))
    if (cont+a)<=100 and cont>=0:
        cont=cont+a
    if (cont+a)>=100:
        v=cont-100
        cont=cont-v
print(cont)