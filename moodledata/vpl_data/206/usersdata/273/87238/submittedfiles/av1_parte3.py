# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('Digite o valor de n: '))
soma=0
termo=1
while termo<=n:
    if termo%2!=0:
        soma=soma+(1)/(termo)*3**(termo-1)
    else:
        soma=soma-(1)/(termo)*3**(termo-1)
        termo=termo+1
print(soma*(12**0.5))
    
    
    
