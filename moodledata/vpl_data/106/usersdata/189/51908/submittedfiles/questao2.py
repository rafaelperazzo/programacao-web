# -*- coding: utf-8 -*-
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
d=int(input('digite o valor de d:'))
e=int(input('digite o valor de e:'))
f=int(input('digite o valor de f:'))
xa=int(input('digite o valor de xa:'))
xb=int(input('digite o valor de xb:'))
xc=int(input('digite o valor de xc:'))
xd=int(input('digite o valor de xd:'))
xe=int(input('digite o valor de xe:'))
xf=int(input('digite o valor de xf:'))
cont=0
if a==xa or a==xb or a==xc or a==xd or a==xe or a==xf:
    cont=cont+1
if b==xa or b==xb or b==xc or b==xd or b==xe or b==xf:
    cont=cont+1
if c==xa or c==xb or c==xc or c==xd or c==xe or c==xf:
    cont=cont+1
if d==xa or d==xb or d==xc or d==xd or d==xe or d==xf:
    cont=cont+1
if e==xa or e==xb or e==xc or e==xd or e==xe or e==xf:
    cont=cont+1
if f==xa or f==xb or f==xc or f==xd or f==xe or f==xf:
    cont=cont+1
if cont==6:
    print('sena')
if cont==5:
    print('quina')
if cont==4:
    print('quadra')
if cont==3:
    print('terno')
if cont==2:
    print('azar')
if cont==1:
    print('azar')
if cont==0:
    print('azar')
