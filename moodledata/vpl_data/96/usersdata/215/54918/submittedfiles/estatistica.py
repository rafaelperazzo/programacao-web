# -*- coding: utf-8 -*-
a=[]
b=[]
somaA=0
difquadA=0
sdqA=0
somaB=0
difquadB=0
sdqB=0
for z in range (1,n+1,1):
    valorA=float(input('valor listaA:'))
    a.append(valorA)
for i in range (0,len(a),1):
    somaA=somaA=a[i]
mediaA=somaA/len(a)
for j in range (0,len(a),1):
    difquadA=(a[j]-mediaA)**2
    sdqA=sqdA+difquadA
varA=sdqA/(len(a)-1)
devioA=varA**0.5
for z in range (1,n+1,1):
    valorB=float(input('valor listaB:'))
    b.append(valorB)]
for i in range (0,len(a),1):
    somaB=somaB=b[i]
mediaB=somaB/len(b)
for j in range (0,len(a),1):
    difquadB=(b[j]-mediaB)**2
    sdqB=sqdB+difquadB
varB=sdqB/(len(b)-1)
devioB=varB**0.5

print('%.2f' %mediaA)
print('%.2f' %devioA)
print('%.2f' %mediaB)
print('%.2f' %devioB)