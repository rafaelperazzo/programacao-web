# -*- coding: utf-8 -*-
from __future__ import division
import funcoes


def valorAbsoluto(x):
    if (x<0):
        return (-1)*x
    else:
        return x
        
    

def pi(m):
    pi=3
    for i in range(1,m+1,1):
        pi=pi+(((-1)**(i+1))*4)/((2*i)*(2*i*1)*(2*i*2))
        return pi
        
        

def fat(x):
    fat=1
    while (x>0):
        fat=x*fat
        x=x-1
    return fat
    
    

def co_seno(z,ep):
    co_z=1
    i=1
    while(co_z>=-1 and co_z<=1):
        g=(((-1)**i)*((z)**(2*i)))/(fat(2*i))
        f=valorAbsoluto(g)
        if (f<ep):
            break
        else:
            co_z= co_z + g
        i= i+1
    return co_z
    
    

def razaoaurea(m,ep):
    gradiente=(pi(m))/5
    razao=2*(co_seno(gradiente,ep))
    return razao
    
   
print('funcao para calcular a razao aurea:')
print('para calcular a razao aurea tem-se que ter dois parametros:')
print('k=numero de termos de pi,tal que k E[1;2000].')
print('e=termo limite do cosseno,tal que e E ]0,1[.')

k=input('digite o valor de k:')
while(k<1 or k>2000):
    print('o valor de k nao pertence ao intervalo:')
    k=input('digite o valor de k:')
    
e=input('digite o valor de e:')
while(e<=0 or e>=1):
    print('o valor de e não pertence ao intervalo:')
    e=input('digite o valor de e:')
    
print ('%.15f' %pi(k))
print ('%.15f' %razaoaurea((k,e))
    