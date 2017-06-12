# -*- coding: utf-8 -*-


def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado
    
def dp(lista):
    soma=0
    for i in range(1,len(lista),1):
        soma=soma+((lista[i]-media(lista))**2)
    resultado=(soma/(len(lista)-1))**1/2
    return resultado
n=int(input('digite o numero de elementos :'))
lista a=[]
lista b=[]
for i in range(1,n+1,1):
    valor1=int(input('digite o valor dos elementos da primeira lista :'))
    lista a.append(valor1)
for i in range(1,n+1,1):
    valor2=int(input('digite o valor dos elementos da segunda lista :'))
    lista b.append(valor2)
print('%.2f'%media(lista a))
print('%.2f'%dp(lista a))
print('%.2f'%media(lis))
print('%.2f'%desvioB)    
    
        











n=int(input('digite o valor de n :'))
a=[]
b=[]
somaA=0
difquadA=0
sdqA=0
somaB=0
difquadB=0
sdqB=0
for z in range(1,n+1,1):
    valorA=float(input('lista A :'))
    a.append(valorA)
for i in range(0,len(a),1):
    somaA=somaA+a[i]
mediaA=somaA/len(a)
for j in range(0,len(a),1):
    difquadA=(a[j]-mediaA)**2
    sdqA=sdqA+difquadA
varA=sqdA/(len(a)-1)
desvioA=varA**1/2
for z in range(1,n+1,1):
    valorB=float(input('lista B :'))
    b.append(valorB)
for i in range(0,len(b),1):
    somaB=somaB+b[i]
mediaB=somaB/len(b)
for j in range(0,len(b),1):
    difquadB=(b[j]-mediaB)**2
    sdqB=sdqB+difquadB
varB=sqdB/(len(b)-1)
desvioB=varB**1/2
print('%.2f'%mediaA)
print('%.2f'%desvioA)
print('%.2f'%mediaB)
print('%.2f'%desvioB)
    