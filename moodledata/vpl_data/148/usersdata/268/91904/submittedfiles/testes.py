# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n '))
a=[]
multiplicacao=1
b=0
for i in range(0,n,1):
    valor=int(input('Digite o valor'))
    a.append(valor)
    if a[0]>a[1] and b==0:
        cont=cont+1
    b=b+1
    if a[n] > a[n-1] and b==1:
        cont=cont+1
    b=b+1
for i in range(0,len(a),1):
     a[i+1] > a[i] and a[i+1] > a[i+2]
if cont!=1 :
    print('N')
else: print('S')