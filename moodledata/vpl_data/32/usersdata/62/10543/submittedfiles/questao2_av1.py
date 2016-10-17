# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

#ENTRADA
a=int(input('Primeiro numero apostado: '))
b=int(input('Segundo numero apostado: '))
c=int(input('Terceiro numero apostado: '))
d=int(input('Quarto numero apostado: '))
g=int(input('Quinto numero apostado: '))
f=int(input('Sexto numero apostado: '))
q=int(input('Primeiro numero sorteado: '))
w=int(input('Segundo numero sorteado: '))
e=int(input('Terceiro numero sorteado: '))
r=int(input('Quarto numero sorteado: '))
t=int(input('Quinto numero sorteado: '))
y=int(input('Sexto numero sorteado: '))
contador=0
#PROCESSAMENTO
if a==q or b==q or c==q or d==q or g==q or f==q:
    contador=contador+1
if a==w or b==w or c==w or d==w or g==w or f==w:
    contador=contador+1
if a==e or b==e or c==e or d==e or g==e or f==e:
    contador=contador+1
if a==r or b==r or c==r or d==r or g==r or f==r:
    contador=contador+1
if a==t or b==t or c==t or d==t or g==t or f==t:
    contador=contador+1
if a==y or b==y or c==y or d==y or g==y or f==y:
    contador=contador+1
#SAIDA
if contador==3:
    print ("terno")
if contador==4:
    print ("quadra")
if contador==5:
    print ("quina")
if contador==6:
    print ("sena")
if contador<3:
    print ("azar")