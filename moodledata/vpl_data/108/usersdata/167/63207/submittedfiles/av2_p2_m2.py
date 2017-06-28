# -*- coding: utf-8 -*-
def vi(lista,y1,y2):
    vi=0
    for i in range (y1,y2+1,1):
        vi=vi+lista[i]
    return vi
n=int(input('digite qnts salas:'))
x=[]
for i in range(0,n,1):
    z=int(input('digite qnts vi:'))
    x.append(z)
w=int(input('digite entrada:'))
k=int(input('digite saida:'))
print(vi(a,b,c))
    