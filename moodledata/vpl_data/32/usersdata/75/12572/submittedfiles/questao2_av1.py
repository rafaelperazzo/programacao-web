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

if (a==na) or (a==nb) or (a==nc) or (a==nd) or (a==ne) or (a==nf):
    cont=cont+1
if (b==na) or (b==nb) or (b==nc) or (b==nd) or (b==ne) or (b==nf):
    cont=cont+1
if (c==na) or (c==nb) or (c==nc) or (c==nd) or (c==ne) or (c==nf):
    cont=cont+1
if (d==na) or (d==nb) or (d==nc) or (d==nd) or (d==ne) or (d==nf):
    cont=cont+1
if (e==na) or (e==nb) or (e==nc) or (e==nd) or (e==ne) or (e==nf):
    cont=cont+1
if (f==na) or (f==nb) or (f==nc) or (f==nd) or (f==ne) or (f==nf):
    cont=cont+1
    
if cont==3:
    print ('terno')
if cont==4:
    print ('quadra')
if cont==5:
    print ('quina')
if cont==6:
    print ('sena')
if (cont!=3) and (cont!=4) and (cont!=5) and (cont!=6):
    print ('azar') 






