# -*- coding: utf-8 -*-

def pico(a):
    if len(a)%2==0:
        x=len(a)//2-1
    else:
        x=len(a)//2
    for i in range (1,x+1,1):
        if a[i]<a[i-1]:
            return False
        else:
            for i in range (x+1,len(a),1):
                if a[i]>a[i-1]:
                    return False
    return True

n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range (0,n,1):
    valor=float(input('Valor:'))
    a.append(valor)
if pico(a):
    print('S')
else:
    print('N')