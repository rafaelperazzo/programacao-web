# -*- coding: utf-8 -*-
n=int(input('escreva n:'))
a=[]
b=[]
somaA=0
difquadA=0
sdqA=0
somaB=0
difquadB=0
sdqB=0
for z in range(1,n+1,1):
    valorA=float(input('valor da lista A:'))
    a.appemd(valorA)
for i in range (0,len(a),1):
    somaA=somaA+a[i]
mediaA=somaA/len


