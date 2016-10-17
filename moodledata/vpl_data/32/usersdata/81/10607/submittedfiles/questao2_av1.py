# -*- coding: utf-8 -*-
from __future__ import division

n1=int(input('Digite o valor do primeiro número:'))
n2=int(input('Digite o valor do segundo número:'))
n3=int(input('Digite o valor do terceiro número:'))
n4=int(input('Digite o valor do quarto número:'))
n5=int(input('Digite o valor do quinto número:'))
n6=int(input('Digite o valor do sexto número:'))
s1=int(input('Digite o valor do primeiro número sorteado:'))
s2=int(input('Digite o valor do segundo número sorteado:'))
s3=int(input('Digite o valor do terceiro número sorteado:'))
s4=int(input('Digite o valor do quarto número sorteado:'))
s5=int(input('Digite o valor do quinto número sorteado:'))
s6=int(input('Digite o valor do sexto número sorteado:'))

cont=0

if n1==s1 or n1==s2 or n1==s3 or n1==s4 or n1==s5 or n1==s6:
    cont=cont+1
    
if n2==s1 or n2==s2 or n2==s3 or n2==s4 or n2==s5 or n2==s6:
    cont=cont+1

if n3==s1 or n3==s2 or n3==s3 or n3==s4 or n3==s5 or n3==s6:
    cont=cont+1
    
if n4==s1 or n4==s2 or n4==s3 or n4==s4 or n4==s5 or n4==s6:
    cont=cont+1
    
if n5==s1 or n5==s2 or n5==s3 or n5==s4 or n5==s5 or n5==s6:
    cont=cont+1
    
if n6==s1 or n6==s2 or n6==s3 or n6==s4 or n6==s5 or n6==s6:
    cont=cont+1

if cont<