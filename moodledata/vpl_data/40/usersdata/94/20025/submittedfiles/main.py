# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

def fatorial(n):
    produto=1
    for i in range(1,n+1,1):
        produto=produto*i
    return produto
        
 

def valor_absoluto(c):
    valor_absoluto = ((c**2)**0.5)
    return valor_absoluto
    

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
    

def cosseno(p,epsilon):
    
    termo=1
    soma=0
    r=2
    g=1
        
    while True: 
        if epsilon<=termo:
            if g%2==0:
                soma=soma-(termo)
            
            else:
                soma=soma+(termo)
        
            
        else:
            break
                    
        termo=(p**r)/fatorial(r)
        r=r+2
        g=g+1
    return soma
        


def razao_aurea(m,epsilon):
    razao=2*(cosseno(pi(m)/5,epsilon))
    return razao
    
m=int(input('digite o numero m de termos da formula de pi:'))
epsilon=input('digite o epsilon para o calculo da razao aurea:')
s=razao_aurea(m,epsilon)

print ('%.15f' %pi(m))
print ('%.15f' %s)



    
    

