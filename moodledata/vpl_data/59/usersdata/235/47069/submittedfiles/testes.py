# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
m=int(input('n:'))
soma=0
n=1
for i in range(1,n+1,1):
    if i%2==0:
        soma=soma-(n/n**2)
    else:
        soma=soma+(n/n**2)
        n=n+1
print(soma)

    