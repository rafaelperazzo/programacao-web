# -*- coding: utf-8 -*-

#FUNÇÃO MÓDULO
def modulo(x):
    y=[]
    for i in range(0,len(x),1):
        if x[i]<0:
            y.append(-1*x[i])
        else:
            y.append(x[i])
    return(y)

#FUNÇÃO MAIOR DIFERENÇA
def diferenca(b):
    maior=b[1]-b[0]
    for i in range(2,len(b),1):
        if (b[i]-b[i-1])>maior:
            maior=(b[i]-b[i-1])
    return(maior)

#PROGRAMA PRINCIPAL
n=0
while n<2:
    n=int(input('Digite o número de termos: '))
a=[]
for i in range(0,n,1):
    numero=(int(input('Digite o %d° termo: ' %(i+1))))
    a.append(numero)
b=modulo(a)

#SAÍDA
print(diferenca(b))
