# -*- coding: utf-8 -*-

n=int(input('Digite o número de pessoas que passaram pela escada rolante: '))
a=[]
for i in range (0,n,1):
    a.append(int(input('Digite o instante de tempo que a pessoa passou: ')))

resultado=0
for j in range (0,len(a),1):
    if j==0:
        resultado=resultado+0
    else:
        resultado=resultado+(a[j]-a[j-1])
resposta=resultado+10
print(resposta)
    
