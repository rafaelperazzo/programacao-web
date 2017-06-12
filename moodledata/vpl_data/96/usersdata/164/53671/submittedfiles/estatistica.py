# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
a=[]
b=[]
somaA=0
difquadA=0
sdqA=0
for z in range (1, n+1, 1):
    valorA=float(input('Valor da lista A: '))
    a.append(valorA)
for i in range (0, len(a), 1):
    somaA=somaA+a[i]
mediaA=somaA/len(a)
for j in range (0, len(a), 1):
    difquadA=(a[j]-mediaA)**2
    sqdA=sqdA+difquadA
desvioA=sqdA/len(a)
print(mediaA)
print(desvioA)
    
    

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 