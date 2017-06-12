# -*- coding: utf-8 -*-
def degrau(a):
    maior=0
    for i in range (0,len(a),1):
        degrau=abs(a[i]-a[i+1])
        if degramau>maior:
            maior=degrau
    return maior

n=int(input('Tamanho da lista:')    
a=[]
for i in range (0,n,1):
    valor=float(input('Valor:'))
    a.append(valor)

print(degrau(a))    
