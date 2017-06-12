# -*- coding: utf-8 -*-

def pico(lista):
    for i in range (1,(len(a)//2)+1,1):
        if a[i]<a[i-1]:
            return False
        else:
            for i in range ((len(a)//2)+1,len(a),1):
                if a[i]>a[i-1]:
                    return False
    return True

n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range (0,n,1):
    valor=float(input('Valor:'))
    a.append(valor)
if pico(a):
    print('É pico')
else:
    print('Não é pico')