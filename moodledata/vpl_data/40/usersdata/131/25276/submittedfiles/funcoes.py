# -*- coding: utf-8 -*-
from __future__ import division
    


# O calculo do valor absoluto >CVA
def CVA(m):
    if m<0:
        return m
        
# Fatorial 

def fatorial(m):
    m_fat=1
    for i in range(2,m+1,1):
        m_fat=m_fat*i
    
    return m_fat
    
#Para o Pi > CPI

def calculopi(m):
    soma_pi=0
    j=2
    for i in range (0,int(m),1):
        if i%2==0:
            soma_pi=soma_pi + (4/(j*(j+1)*(j+2)))
        else:
            soma_pi=soma_pi - (4/(j*(j+1)*(j+2)))
        j = j + 2 
        pi=3+soma_pi
        
        return pi
        
# calculo do cosseno > CCOS

def CCOS(z,e):
    soma_cosseno=0
    i=1
    j=2
    x=(z**j)/fatorial(j)
    while x>e:
        x=(z**j)/fatorial(j)
        if i%2 !=0 :
            soma_cosseno=soma_cosseno + x
        else:
            soma_cosseno=soma_cosseno - x
        j=j+2
        i=i+1
    cos=1-soma_cosseno
    
    return cos
    
# calculo da razãoaurea >CRA

def CRA (m,e):
    pi= CPI(m)
    cos= CCOS(pi/5,e)
    razaoaurea= cos * 2
    
    return razaoaurea 
    
 
    

        
        
        