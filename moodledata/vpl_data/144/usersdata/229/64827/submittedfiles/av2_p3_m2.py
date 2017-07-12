# -*- coding: utf-8 -*-
magica=int(input('digite um valor:'))
n=int(input('digite o tamanho:'))
a=[]
for i in range (0,n,1):
    v=int(input('digite o elemento:'))
    a.append(v)
if magica(a):
    print ('sim')
else:
    print('não')

def magica(lista):
    cont=0
    for i in range(0,len(lista),1):
        if vezes(i,lista)==lista[i]:
            cont=cont+1
    if cont==len(lista):
        return True
    else:
        return False