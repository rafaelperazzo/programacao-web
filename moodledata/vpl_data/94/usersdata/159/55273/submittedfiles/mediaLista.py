# -*- coding: utf-8 -*-
def media(a):
    cont=0
    for i in range (0,len(a),1):
        cont=cont+a[i]
    media=cont/len(a)
    return media

n=int(input('Tamanho da lista:'))
a=[]
for i in range(0,n,1):
    valor=float(input('Valor:'))
    a.append(valor)

print('%.2f'a[0])
print('%.2f'a[len(a)-1])
print('%.2f'media(a))
print(a)

