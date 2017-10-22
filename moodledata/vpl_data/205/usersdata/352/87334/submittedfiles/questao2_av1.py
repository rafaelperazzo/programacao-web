# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=int(input('Digiteo o numero: '))
b=int(input('Digiteo o numero: '))
c=int(input('Digiteo o numero: '))
d=int(input('Digiteo o numero: '))
e=int(input('Digiteo o numero: '))
f=int(input('Digiteo o numero: '))
g=int(input('O numero sorteado: '))
h=int(input('O numero sorteado: '))
i=int(input('O numero sorteado: '))
j=int(input('O numero sorteado: '))
k=int(input('O numero sorteado: '))
l=int(input('O numero sorteado: '))

cont=0

if g%a==0 or g%b==0 or g%c==0 or g%d==0 or g%e==0 or g%f==0:
    cont=cont+1
if h%a==0 or h%b==0 or h%c==0 or h%d==0 or h%e==0 or h%f==0:
    cont=cont+1
if i%a==0 or i%b==0 or i%c==0 or i%d==0 or i%e==0 or i%f==0:
    cont=cont+1
if j%a==0 or j%b==0 or j%c==0 or j%d==0 or j%e==0 or j%f==0:
    cont=cont+1
if k%a==0 or k%b==0 or k%c==0 or k%d==0 or k%e==0 or k%f==0:
    cont=cont+1
if l%a==0 or l%b==0 or l%c==0 or l%d==0 or l%e==0 or l%f==0:
    cont=cont+1
if cont==3:
    print('terno')
if cont==4:
    print('quadra')
if cont==5:
    print('quina')
if cont==6:
    print('sena')
if cont<3:
    print('azar')
    
