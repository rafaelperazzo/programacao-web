#-*- coding: utf-8 -*-
  
v=int(input('digite o volume inicial:'))
a=int(input('digite as alterações feita no volume:'))
 
i=0
cont=v
for i in range(1,a+1,1):
    t=int(input('digite a alteração feita no volume:'))
    if (cont+t)<=100 and cont>=0:
        cont=cont+t
    elif (cont+t)>=100:
        v=cont-100
        cont=cont-v
print (cont)