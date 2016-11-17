# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

    m_fat=1
    for i in range (2,m+1,1):
        m_fat=m_fat * i
    return m_fat
                
m=int(input('Digite m:'))
e=input('Digite o epsilon para o cosseno:')

#DOUBLE CALCULA_VALOR_ABSOLUTO:
if m<0:
    m=m*(-1)

#DOUBLE CALCULA_PI:
soma_pi=0
j=2
for i in range (0,m,1):
    if i%2==0:
        soma_pi=soma_pi+(4/(j*(j+1)*(j+2)))
    else:
        soma_pi=soma_pi-(4/(j*(j+1)*(j+2)))
    j=j+2    
pi=3+soma_pi

#DOUBLE CALCULA_CO_SENO:
soma_cosseno=0
i=1
j=2
a=(( (pi/5) **j) / fatorial (j) )
while a>e:
    if i%2!=0:
        soma_cosseno = soma_cosseno + a
    else:
        soma_cosseno = soma_cosseno - a
    j=j+2
    i=i+1
#CHAMAR A SEGUNDA PARTE DA SOMA_COSSENO DE UMA VARIÁVEL:
'''
a= (((pi/5)**j)/fatorial(j)) e a repetição só iria acontecer enquanto a fosse menor ou igual a epsilon

----> a repetição ocorre apenas enquanto a for MAIOR que epsilon. 


'''    
cosseno=1-soma_cosseno

#DOUBLE CALCULA_RAZAO_AUREA_:
razaoAurea= 2*cosseno
print('%.15f' %pi)
print('%.15f' %razaoAurea)