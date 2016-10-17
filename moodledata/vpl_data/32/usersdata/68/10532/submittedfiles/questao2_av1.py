# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA:
cont=0
A1= input ('Digite o primeiro número apostado:')
A2= input ('Digite o segundo número apostado:')
A3= input ('Digite o terceiro número apostado:')
A4= input ('Digite o quarto número apostado:')
A5= input ('Digite o quinto número apostado:')
A6= input ('Digite o sexto número apostado:')

S1= input ('Digite o primeiro número sorteado:')
S2= input ('Digite o segundo número sorteado:')
S3= input ('Digite o terceiro número sorteado:')
S4= input ('Digite o quarto número sorteado:')
S5= input ('Digite o quinto número sorteado:')
S6= input ('Digite o sexto número sorteado:')

#PROCESSAMENTO:
if A1==S1 or A1==S2 or A1==S3 or A1==S4 or A1==S5 or A1==S6:
    cont=cont+1
if A2==S1 or A2==S2 or A2==S3 or A2==S4 or A2==S5 or A2==S6:
    cont=cont+1
if A3==S1 or A3==S2 or A3==S3 or A3==S4 or A3==S5 or A3==S6:
    cont=cont+1
if A4==S1 or A5==S2 or A4==S3 or A4==S4 or A4==S5 or A4==S6:
    cont=cont+1
if A5==S1 or A5==S2 or A5==S3 or A5==S4 or A5==S5 or A5==S6:
    cont=cont+1
if A6==S1 or A6==S2 or A6==S3 or A6==S4 or A6==S5 or A6==S6:
    cont=cont+1

#SAIDA:
if cont<=2:
    print ('azar')
if cont==3:
    print ('terno')
if cont==4:
    print ('quadra')
if cont==5:
    print ('quina')
if cont==6:
    print ('sena')