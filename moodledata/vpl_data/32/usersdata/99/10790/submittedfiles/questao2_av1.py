# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

a=int(input('Digite um número entre 0 e 99:'))
b=int(input('Digite um número entre 0 e 99:'))
c=int(input('Digite um número entre 0 e 99:'))
d=int(input('Digite um número entre 0 e 99:'))
e=int(input('Digite um número entre 0 e 99:'))
f=int(input('Digite um número entre 0 e 99:'))

u=int(input('Digite o primeiro número sorteado:'))
v=int(input('Digite o segundo número sorteado:'))
w=int(input('Digite o terceiro número sorteado:'))
x=int(input('Digite o quarto número sorteado:'))
y=int(input('Digite o quinto número sorteado:'))
z=int(input('Digite o sexto número sorteado:'))

cont=0

if (a==u) or (a==v) or (a==w) or (a==x) or (a==y) or (a==z):
    cont=cont+1
    
if (b==u) or (b==v) or (b==w) or (b==x) or (b==y) or (b==z):
    cont=cont+1
    
if (c==u) or (c==v) or (c==w) or (c==x) or (c==y) or (c==z):
    cont=cont+1
    
if (d==u) or (d==v) or (d==w) or (d==x) or (d==y) or (d==z):
    cont=cont+1
    
if (e==u) or (e==v) or (e==w) or (e==x) or (e==y) or (e==z):
    cont=cont+1
    
if (f==u) or (f==v) or (f==w) or (f==x) or (f==y) or (f==z):
    cont=cont+1
    
if cont==3:
    print('Terno')
if cont==4:
    print('Quadra')
if cont==5:
    print('Quina')
if cont==6:
    print('Sena')
if cont<3:
    print('Azar')
