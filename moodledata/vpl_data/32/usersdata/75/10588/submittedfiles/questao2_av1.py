# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número:'))
c=int(input('Digite o terceiro número:'))
d=int(input('Digite o quarto número:'))
e=int(input('Digite o quinto número:'))
f=int(input('Digite o sexto número:'))
na=int(input('Digite o primeiro número sorteado:'))
nb=int(input('Digite o segundo número sorteado:'))
nc=int(input('Digite o terceiro número sorteado:'))
nd=int(input('Digite o quarto número sorteado:'))
ne=int(input('Digite o quinto número sorteado:'))
nf=int(input('Digite o sexto número sorteado:'))

cont=0

if a==na:
    cont=cont+1
    cont=cont
if b==na:
    cont=cont+1
    cont=cont
if c==nc:
    cont=cont+1
    cont=cont
if d==nd:
    cont=cont+1
    cont=cont
if e==ne:
    cont=cont+1
    cont=cont
if f==nf:
    cont=cont+1
    cont=cont
    
if cont==3:
    print ('terno')
if cont==4:
    print ('quadra')
if cont==5:
    print ('quina')
if cont==6:
    print ('seno')
if (cont!=3) and (cont!=4) and (cont!=5) and (cont!=6):
    print ('azar') 






