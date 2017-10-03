# -*- coding: utf-8 -*-
import math
#ENTRADA
cv = int(input('Digite a quantidade de vitorias: '))
ce = int(input('Digite a quantidade de empates: '))
cd = int(input('Digite a quantidade de derrotas: '))
fv = int(input('Digite a quantidade de vitorias: '))
fe = int(input('Digite a quantidade de empates: '))
fd = int(input('Digite a quantidade de derrotas: '))
#PROCESSAMENTO
pc = (3*cv)+(1*ce)
pf = (3*fv)+(1*fe)
if pc>pf :
    print('C')
if pf>pc :
    print('F')
if pc==pf and cv>fv :
    print('C')
if pc==pf and fv>cv :
    print('F')

