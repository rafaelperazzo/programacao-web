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
mediaA=somaA/len(a)
for j in range (0,len(a),1):
    difquadA=(a[j]-mediaA)**2
    sdqA=sdqA+difquadA
varA=sdqA/(len(a)-1)
desvioA=varA**0.5

for z in range (1,n+1, 1):
    valorB=float(input('valor da lista B:'))
    b.append(valorB)
for i in range (0,len(b), 1):
    somaB=somaB+b[i]
mediaB=somaB/len(b)
for j in range (0,len(b), 1):
    difquadB=(b[j]-mediaB)**2
    sddB=sdqB+difquadB
varB=sdqB/len(b)-1)
desvioB=varB**0.5


print('%.2f' %mediaA)
print('%.2f' %desvioA)
print('%.2f' %mediaB)
print('%.2f' %desvioB)


