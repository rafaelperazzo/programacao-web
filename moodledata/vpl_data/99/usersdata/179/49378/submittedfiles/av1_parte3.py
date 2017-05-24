# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('digite o valor de n :'))
soma=0
i=0
m=1
termo=1
while termo<=n:
    if i%2==0:
        soma=soma+(1/m*(3**i))
    else:
        soma=soma-(1/m*(3**i))
    pi=(12**1/2)*soma    
    i=i+1
    m=m+2
    termo=termo+1
print('%.6f'%pi)    
    
        
