# -*- coding: utf-8 -*-
def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
        
    media=soma/len(a)
    return(media)
    
    
n=int(input('digite a quantidade de elementos da lista:'))
a=[]
for i in range(1,n+1,1):
    valor=float(input('digite um valor:'))
    a.append(valor)
    
print('%.2f' %a[0])
print('%.2f' %a[len(a)-1])
print('%.2f' %media(a))
print(a)