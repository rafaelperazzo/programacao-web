# -*- coding: utf-8 -*-

n=int(input('Digite n: '))
a=[]
b=[]
contA=0
contB=0
for z in range (1, n+1, 1):
    valorA=float(input('Valor da lista A:'))
    a.append(valorA)
for i in range (1, n+1, 1):
    if (i==0):
        if (a[ai]>a[i]):
            contA=contA+1
    elif (i==len(a)-1):      
        if (a[i]>a[i-1]):
            contA=contA+1
    else:
        if (a[i]>a[i+1] and a[i]>a[i-1]):
            contA=contA+1
            
for z in range (1, na+1, 1):
    valorB=float(input('Valor da lista B: '))
    b.append(valorB)
for i in range (0,len(b), 1):
    if (i==0):
        if (b[i]>b[i+1]):
            contB=contB+1
    elif (i==len(b)-1):
        
        
        


