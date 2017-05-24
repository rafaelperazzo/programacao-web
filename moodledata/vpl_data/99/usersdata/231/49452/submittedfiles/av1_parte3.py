# -*- coding: utf-8 -*-

v=int(input('digite v:'))
soma=0
b=1
for i in range(0,v+1,1):
    if i%2==0:
        soma=soma+(1/(b*(3**i)))
        b=b+2
    else:
        soma=soma-(1/(b*(3**i)))
d=(12**(1/2))*soma
print('%.6f'%d)
