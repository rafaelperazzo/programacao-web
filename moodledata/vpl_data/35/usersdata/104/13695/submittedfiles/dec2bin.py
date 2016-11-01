# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
p=input('Digite o número p:')
q=input('Digite o número q:')
i=1
j=1
cp=0
cq=0
cont=0
#PROCESSAMENTO
while p//i>0:
    cp=cp+1
    i=i*10
while q//j>0:
    cq=cq+1
    j=j*10
pp=10**(cp-1)
pq=10**(cq-1)
while q//pq>0:
    if q%pq==p%pp:
        pp=pp/10
        cont=cont+1
pq=pq/10
#SAÍDA
if cont==cp:
    print('S')
else:
    print('N')
