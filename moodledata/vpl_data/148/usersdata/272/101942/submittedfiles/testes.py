# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n=int(input('Digite o número de termos: '))
a=[]
for i in range (0,n,1):
    a.append(float(input('Digite o valor: ')))
soma=0
for j in range (0,len(a),1):
    soma=soma+a[j]
media=soma/len(a)
delta=0
for k in range (0,len(a),1):
    delta=delta+((a[k]-media))**2
desvpad=((1/(len(a))*(len(a)-1))*delta)**(1/2)
print(desvpad)
    

