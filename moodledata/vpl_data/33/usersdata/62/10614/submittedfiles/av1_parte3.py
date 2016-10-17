# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
#ENTRADA
n=input("Digite o valor de n: ")
j=1
k=0
i=1
soma=0
pi=(12**0.5)
#PROCESSAMENTO
while i<=n:
    if i%2==0:
        soma=soma-(1/j*(3**k))
    else:
        soma=soma+(1/j*(3**k))
    j=j+2
    i=i+1
    k=k+1
total=pi*soma
print ("o valor de pi é: %.6"%total)