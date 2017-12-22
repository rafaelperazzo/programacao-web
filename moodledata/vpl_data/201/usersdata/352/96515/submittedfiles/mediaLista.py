# -*- coding: utf-8 -*-

def soma(a):
    total=0
    for i in range(0, len(a), 1):
        total=total+a[i]
    return (total)
    
def media(a):
    return(soma(a)/len(a))


n=int(input('Quantidade de elementos: '))
a=[ ]

for i in range(0,n,1):
    valor=float(input('Valor: '))
    a.append(valor)
    
print('%.2f' %a[0])
print('%.2f' %a[len(a)-1])
print('%.2f' %media(a))
print('%.1f' %a)