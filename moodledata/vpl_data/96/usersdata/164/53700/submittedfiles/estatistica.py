# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
a=[]
b=[]
somaA=0
difquadA=0
sdqA=0
somaB=0
difquadB=0
sdqB=0
for z in range (1, n+1, 1):
    valorA=float(input('Valor da lista A: '))
    a.append(valorA)
for i in range (0, len(a), 1):
    somaA=somaA+a[i]
mediaA=somaA/len(a)
for j in range (0, len(a), 1):
    difquadA=((a[j]-mediaA)**2)
varA=difquadA/len(a)
desvioA=varA**1/2

for z in range (1, n+1, 1):
    valorB=float(input('Valor da lista B: '))
    b.append(valorB)
for i in range (0, len(b), 1):
    somaB=somaB+b[i]
mediaB=somaB/len(b)
for j in range (0, len(b), 1):
    difquadB=(a[j]-mediaB)**2
    sdqB=sdqB+difquadB
varB=sdqB/len(b)
desvioB=varB**1/2


print('%.2f' %mediaA)
print('%.2f' %desvioA)
print('%.2f' %mediaB)
print('%.2f' %desvioB)


#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 