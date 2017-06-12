 -*- coding: utf-8 -*-
 n=int(input('Digite n'))
 t=int(input('Digite t:'))
 i=0
 soma=n
 a=[]
 for i in range(1,t+1,1):
     p=int(input('Digite p:'))
     a.append(p)
     
for i in range(0,len(a),1):
    if soma>100:
        soma=100
    elif soma<0:
        soma=0
print(soma)