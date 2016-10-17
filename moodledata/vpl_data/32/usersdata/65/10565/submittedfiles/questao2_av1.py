# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

#NUMEROS
n1=input('Digite o primeiro número: ')
n2=input('Digite o segundo número: ')
n3=input('Digite o terceiro número: ')
n4=input('Digite o quarto número: ')
n5=input('Digite o quinto número: ')
n6=input('Digite o sexto número: ')

#SORTEADOS
s1=input('Digite o primeiro número sorteado : ')
s2=input('Digite o segundo número sorteado : ')
s3=input('Digite o terceiro número sorteado : ')
s4=input('Digite o quarto número sorteado : ')
s5=input('Digite o quinto número sorteado : ')
s6=input('Digite o sexto número sorteado : ')


contador=0

#SORTEIO

if (n1==s1 or n1==s2 or n1==s3 or n1==s4 or n1==s5 or n1==s6):
    contador=contador+1

if (n2==s1 or n2==s2 or n2==s3 or n2==s4 or n2==s5 or n2==s6):
    contador=contador+1

if (n3==s1 or n3==s2 or n3==s3 or n3==s4 or n3==s5 or n3==s6):
    contador=contador+1

if (n4==s1 or n4==s2 or n4==s3 or n4==s4 or n4==s5 or n4==s6):
    contador=contador+1
    
if (n5==s1 or n5==s2 or n5==s3 or n5==s4 or n5==s5 or n5==s6):
    contador=contador+1
    
if (n6==s1 or n6==s2 or n6==s3 or n6==s4 or n6==s5 or n6==s6):
    contador=contador+1

#RESULTADO

if (contador==3):
    print('terno')

if (contador==4):
    print('quadra')
    
if (contador==5):
    print('quina')
    
if (contador==6):
    print('sena')
    
if (contador<3):
    print('azar')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    