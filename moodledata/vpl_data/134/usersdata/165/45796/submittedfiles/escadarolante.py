# -*- coding: utf-8 -*-
n=int(input('digite o numero de pessoas:'))
a=int(input('digite o primeiro tempo:'))
cont=10
for i in range(2,n+1,1):
   t=int(input('digite o tempo que a pessoa entrou:'))
   x=t-a
   cont=cont+x
print(cont) 
   
    