# -*- coding: utf-8 -*-
def sala(a):
    for i in range(0,len(a),1):
        if a[i]>a[i+1]:
            soma=soma+(a[i])
    return soma
        
n=int(input('Digite quantidade de salas:'))
a=[]
for i in range(0,n,1):
    valor=int(input('Digite vida da sala:'))
    a.append(valor)
pe=int(input('Digite porta de entrada:'))
ps=int(input('Digite porta de saida:'))

print(sala(a))
    
    
