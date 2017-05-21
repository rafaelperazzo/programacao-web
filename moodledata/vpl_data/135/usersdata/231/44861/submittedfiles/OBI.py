# -*- coding: utf-8 -*-
n=int(input('digite número de competidores :'))
p=int(input('digite número de pontos necessários :'))
cont=0
for i in range(1,n+1,1):
    x=int(input('digite número de pontos prova 1 :'))
    y=int(input('digite número de pontos prova 2 :'))
    if (x+y)>=p:
        cont=cont+1
print(cont)








