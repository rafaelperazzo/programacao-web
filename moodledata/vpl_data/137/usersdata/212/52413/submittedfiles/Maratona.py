# -*- coding: utf-8 -*-
n=int(input('digite o número de postes:'))
m=int(input('digite a distância maxima do corredor:'))
ant=0
cont=1
while i<=n:
    x=int(input('digite a distância do proximo poste:'))
    distancia=x-ant
    if distancia<=m:
        cont=cont+1
    ant=x
    i=i+1
if cont==n+1:
    print('S')
else:
    print(N)