# -*- coding: utf-8 -*-
def tempo (a) :
    intervalo=10
    for i in range(1,len(a),1):
        intervalo=intervalo+(a[i]-a[i-1])
    return (intervalo)
    
n=int(input('número de pessoas'))
lista=[]
for i in range (0,n,1):
    lista.append(int(input('instante da %d pessoa:' %(i+1))))
print (tempo(lista))