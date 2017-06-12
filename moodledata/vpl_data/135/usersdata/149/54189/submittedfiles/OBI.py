# -*- coding: utf-8 -*-
n=int(input('digite quantos competidores: '))
p=int(input('digite o mínimo para receber o convite:'))
pontos=0
cont=0
for i in range(1,n+1,1):
    s1=int(input('pontos na primeira fase:'))
    s2=int(input('pontos na segunda fase:'))
    pontos=s1+s2
    if (pontos>=p):
        cont=cont+1
print(cont)