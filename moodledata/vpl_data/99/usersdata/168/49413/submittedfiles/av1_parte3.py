# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('Digite o valor de n: '))
pi=0
i=1
f=3
for termo in range(1,n+1,1):
    if termo%2==1:
        pi=pi+1/(i*(3**(f)))
    else:
        pi=pi-1/(i*(3**(f)))
    i=i+2
    pi=pi*(12**(1/2))
print('%.6f'%pi)    
