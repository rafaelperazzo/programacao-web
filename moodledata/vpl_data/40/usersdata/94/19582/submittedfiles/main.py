# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
#fazendo um fatorial 

def fatorial(n):
   if n<=1:
      return 1
   else: 
      return n*fatorial(n-1) 

#estou fazendo agora o valor absoluto 

def valor_absoluto(c):
    valor_absoluto = ((c**2)**0.5)
    return valor_absoluto
    
#agora o pi

def pi(m):
    soma=0
    j=2
    for i in range(1,m+1,1):
        if i%2==0:
            soma=soma-(4/(j*(j+1)*(j+2)))
        else:
            soma=soma+(4/(j*(j+1)*(j+2)))
        j=j+2
    soma=soma+3
    return soma 
    
#cosseno 

def cosseno(p,epsilon):
    
    termo=1
    soma=0
    r=2
    g=1
        
    while True: 
        if epsilon<=termo:
            if g%2==0:
                soma=soma-termo
            
            else:
                soma=soma+termo
            
        if epsilon>termo:
            break
                    
        termo=(p**r)/fatorial(r)
        r=r+2
        g=g+1
    return soma


def razao_aurea(m,epsilon):
    razao=2*(cosseno(pi(m)/5,epsilon))
    return razao
    
m=int(input('digite m:'))
epsilon=input('digite epsilon:')
s=razao_aurea(m,epsilon)
p=pi(m)
print ('%.15f' %p)
print ('%.15f' %s)



    
    

