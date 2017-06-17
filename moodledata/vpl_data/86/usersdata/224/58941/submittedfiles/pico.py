# -*- coding: utf-8 -*-

def pico(a):
    cont=0
    for i in range(0,len(a)//2,1):
        if lista[i]>lista[i+1]:
            return False
    for i in range(len(a)//2 +1,len(a),1):
        if lista[i]<lista[[i-1]:
            cont=cont+1
            
    if cont==len(a)//2:
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