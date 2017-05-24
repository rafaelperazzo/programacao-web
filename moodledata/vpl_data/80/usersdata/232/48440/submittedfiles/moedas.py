# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de c: '))
cont=0
soma=0
toto=0
eoq=0

for i in range (1,c+1,1):
    if c%a==0:
        x1=c//a
        y1=(c%a)/b
        cont=cont+1
        soma=soma+1
        toto=toto+1
        eoq=eoq+1
    elif c%b==0:
        x2=(c//b)
        y2=(c%b)/a
        cont=cont+1
        soma=soma+1
        toto=toto+1
        eoq=eoq+0
        
    elif c%a!=0:
        x3=(c%a)/b
        y3=c//a
        cont=cont+1
        soma=soma+1
        toto=toto+0
        eoq=eoq+0
        
    elif c%b!=0:
        x4=(c%b)/a
        y4=c//b
        cont=cont+1
        soma=soma+0
        toto=toto+0
        eoq=eoq+0
    
if cont>0 and soma>0 and toto>0 and eoq>0:
    print('%d' %x1)
    print('%d' %y1)

elif cont>0 and soma>0 and toto>0 and eoq==0:
    print('%d' %x2)
    print('%d' %y2)
    
elif cont>0 and soma>0 and toto==0 and eoq==0:
    print('%d' %x3)
    print('%d' %y3)
    
elif cont>0 and soma==0 and toto==0 and eoq==0:
    print('%d' %x4)
    print('%d' %y4)
    
else:
    print('N')
    
    
        
    
