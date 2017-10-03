# -*- coding: utf-8 -*-
import math
#ENTRADA
cv = int(input('Digite a quantidade de vitorias: '))
ce = int(input('Digite a quantidade de empates: '))
cs = int(input('Digite o saldo de gols: '))
fv = int(input('Digite a quantidade de vitorias: '))
fe = int(input('Digite a quantidade de empates: '))
fs = int(input('Digite o saldo de gols: '))
#PROCESSAMENTO
pc = (3*cv)+(1*ce)
pf = (3*fv)+(1*fe)
if pc>pf :
    print('C')
if pf>pc :
    print('F')
if pc==pf and cs>fs :
    print('C')
if pc==pf and fs>cs :
    print('F')
if pc==pf and cs==fs and cv>fv :
    print('C')
if pc==pf and cs==fs and fv>cv :
    print('F')
if pc==pf and cs==fs and fv==cv

