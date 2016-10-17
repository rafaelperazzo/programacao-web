# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
#ENTRADA
cont=0
#numeros apostados
a=input('insira um numero entre 1 e 99:')
b=input('insira um numero entre 1 e 99:')
c=input('insira um numero entre 1 e 99:')
d=input('insira um numero entre 1 e 99:')
e=input('insira um numero entre 1 e 99:')
f=input('insira um numero entre 1 e 99:')
#numeros sorteados
g=input('insira um numero entre 1 e 99:')
h=input('insira um numero entre 1 e 99:')
i=input('insira um numero entre 1 e 99:')
j=input('insira um numero entre 1 e 99:')
k=input('insira um numero entre 1 e 99:')
l=input('insira um numero entre 1 e 99:')
#processamento
if a==g or a==h or a==i or a==j or a==k or a==l:
    cont=cont +1
    if b==g or b==h or b==i or b==j or b==k or b==l:
        cont=cont +1
        if c==g or c==h or c==i or c==j or c==k or c==l:
            cont=cont+1
            if d==g or d==h or d==i or d==j or d==k or d==l:
                cont=cont +1
                if e==g or e==h or e==i or e==j or e==k or e==l:
                    cont=cont+1
                    if f==g or f==h or f==i or f==j or f==k or f==l:
                        cont=cont+1
if cont==6:
    print ('SENA')
if cont==5:
    print('QUINA')
if cont==4:
    print('QUADRA')
if cont==3:
    print('TERNO')
if cont<3:
    print ('AZAR')
    
