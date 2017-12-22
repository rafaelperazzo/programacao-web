# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
for i in range(0,n-1,1):
        p = 0
        h = 0
        if lista[i]<lista[i+1]:
            continue
        else:
            p = lista[i]
            break
        for t in range(p,n-1,1):
            if lista[t]<lista[t+1]:
                h = h + 1
            elif lista[t]>lista[t+1]:
                h = h - 100000000000
    if h>0:
        print('S')
    else:
        return('N')