# -*- coding: utf-8 -*-

def pico(a):
    soma=0
    for i in range(0,len(a)//2,1):
        if a[i]>a[i+1]:
            return False
    for i in range(len(a)//2 +1,len(a),1):
        if a[i]<a[[i-1]:
            soma=soma+1
            
    if soma==len(a)//2:
        return True
    else:
        return False
        
n =int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(1,n+1,1):
    valor=float(input('valores: '))
    a.append(valor)

if pico(a):
    print('S')
else:
    print('N')