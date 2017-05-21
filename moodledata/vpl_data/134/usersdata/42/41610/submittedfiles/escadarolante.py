# -*- coding: utf-8 -*-
n=int(input('digite o numero de pessoas: '))
cont=0
t1=int(input("digite o seundo que a pessoa 1 passou pelo sensor: "))
for i in range (2,n+1,1):
    t2=int(input("digite o seundo que a pessoa %i passou pelo sensor: "%i))
    if (t2-t1)>10:
        cont=cont+10
    else:
        cont=cont+(t2-t1)
    t1=t2
print(cont+10)