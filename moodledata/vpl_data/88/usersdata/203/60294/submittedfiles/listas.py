# -*- coding: utf-8 -*-
def maiordegrau(a):
    l=[]
    for i in range (1,len(lista),1):
        degrau=l[i]-l[i-1]
        if degrau>0:
            degrau=degrau
        else:
            degrau=degrau*(-1)
        l.append(degrau)
    return(max(l))
n=int(input('digite n: '))
lista=[]
for i in range(1,n,1):
    a=float(input('digite a: '))
    lista.append(a)
print('%.d' % maiordegrau(lista))

