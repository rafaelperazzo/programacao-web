#ARQUIVO COM SUAS FUNCOES
from __future__ import division
def pi(x):
    s=3
    a=0
    i1=2
    i2=3
    i3=4
    while(a<x):
        y=((4)/(i1*i2*i3))
        if (i3)%4==0:
            s=s+y
        else:
            s=s-y
        i1=i1+2
        i2=i2+2
        i3=i3+2
        a=a+1
    return s   
def modulo(x):
    if x<0:
        x=x*-1
        return x
    else:
        return x
def fatorial(i):
    fatorial=1
    while(i>=1):
        fatorial=fatorial*i
        i=i-1
    return fatorial 
print(fatorial(5))    
    