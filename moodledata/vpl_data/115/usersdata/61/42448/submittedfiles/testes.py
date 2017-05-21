# -*- coding: utf-8 -*-
from __future__ import division
import math

exc= float(input('Digite o valor de exc: '))
L= float(input('Digite o valor de L: '))

sigma= 40000
pi= math.pi
erro=0.4
a=1
c=1
r=1

pcr=(((pi**2)*erro*a)/(L/r)**2)
p0=pcr/2
x2=0
p01=p0
k=0

while(True):
    
    f=((p0/erro)**0.5)
    x=(1+(exc)*(1/math.cos((1/2)*f)))
   
    fp= p0-(sigma/x)
   
    n=(1*sigma*exc)*(1/math.cos(((1/2)*(p0/erro))**(0.5)))
    m=math.tan((1/2)*(p0/erro)**(0.5))
    s=(4*(erro*p0)**0.5)
    p=(1+exc*(1/math.cos(((1/2)*(P0/erro))**0.5)))**2
    
    fp2= 1+((n*m)/(p*s))
    
    print ('Iteração' + str(k))
    k=k+1
    
    x2=p0-(fp/fp2)
    print (p0,x2)
    
    if abs(p0-x2)<erro:
        print (x2)
        p0=x2
        
f=((x2/erro)**0.5)
x=((1+(exc)*(1/math.cos((1/2)*f))))

fp=f0-(sigma/x)
print('O número substituido na raiz é: ',fp)
print('A raiz é: ',x2)
print('O número de iterações é: ',k)

