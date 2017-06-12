# -*- coding: utf-8 -*-
n=int(input('item n:'))
a=[]
b=[]
somaA=0
difquadA=0
sdqA=0
somaB=0
difquadB=0
sdqB=0
for z in range (1,n+1,1):
    valorA=float(input('valor da lista A:'))
    a.append(valorA)
for i in range (0, len(a), 1):
    somaA=somaA+a[i]
mediaA=somaA+a[i]
for j in range (0, len(a), 1):
    difquadA=(a[j]-mediaA)**2
    sdqA=sdqA+difquadA
varA=sdqA/(len(a)-1)
desvioA=varA**0.5

for z in range (1, n+1, 1):
    valorB=float(input('valor da lista B:')
    b.append(valorB)
for j in range (0, len(b), 1):
    somaB=somB+b[i]
mediaB=somaB/len(B)
FOR J IN RANGE (0, len(b), 1):
    difquadB=(b[j]-mediaB)**2
    sdqB=sdqB+difquadB
varB=sdqB/(len(b)-1)
desvioB=barB**0.5


print('%.2f' %mediaA)
print('%.2f' %desvioA)
print('%.2f' %mediaB
print('%.2f' %desvioB)
print('%.2f' %mediaA)

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 