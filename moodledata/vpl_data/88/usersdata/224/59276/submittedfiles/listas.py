# -*- coding: utf-8 -*-
def degrau(a):
    maior=0
    valor=0
    for i in range(0,len(a),1):
        if abs(a[i]-a[i+1])>maior:
            valor=maior
            maior=maior
    return valor
n=int(input('Digite o tamanho da lista: '))
a=[]
for i in range(1,n+1,1):
    y=int(input('Digite o valor: '))
    a.append(y)
print(degrau(a))
            
        
    

