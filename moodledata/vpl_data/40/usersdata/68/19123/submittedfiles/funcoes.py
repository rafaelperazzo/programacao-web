# -*- coding: utf-8 -*-
from __future__ import division

#Fatorial 
def fatorial (m):
    m_fat=1
    for i in range (2,m+1,1):
        m_fat=m_fat * i
    return m_fat
#Pi
def calculaPi (m):
    soma_pi=0
    j=2
    for i in range (0,m,1):
        if i%2==0:
            soma_pi=soma_pi+(4/(j*(j+1)*(j+2)))
        else:
            soma_pi=soma_pi-(4/(j*(j+1)*(j+2)))
        j=j+2
    pi=3+soma_pi
    return pi
#Cosseno
def calculaCosseno (z,e):
    soma_cosseno=0
    i=1
    j=2
    a=(z**j)/fatorial(j)   #TINHA UM ERRO AQUI  <-------------------- ERRO
    print ("primeiro a: %.4f" %a)
    while a>e:
        a=(z**j)/fatorial(j) # <-------------- TEM Q CALCULAR UM NOVO VALOR DE a A CADA REPETIÇÃO
        if i%2!=0:
            soma_cosseno=soma_cosseno+a
        else:
            soma_cosseno=soma_cosseno-a
        j=j+2
        i=i+1
        print ("a=%.8f soma_cosseno=%.4f" %(a,soma_cosseno))
    cosseno=1-soma_cosseno
    return cosseno
    
#RazaoAurea
def calculaRazaoAurea (cosseno):
    razaoAurea= 2*cosseno
    return razaoAurea