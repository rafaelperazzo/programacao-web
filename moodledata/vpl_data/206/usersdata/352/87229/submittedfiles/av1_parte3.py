# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('Digite o numero de termos: '))

s=0
i=1
j=0

while j<n:
    if j%2==0:
        s= s+(1/(i*(3**j))
    else:
        s=s-(1/(i*(3**j))
    i=i+2
    j=j+1
pi=(12**0.5)*s
print('%.6f'%pi)