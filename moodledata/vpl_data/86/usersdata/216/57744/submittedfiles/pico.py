# -*- coding: utf-8 -*-


def pico(x):
    for i in range(0,len(x),1):
        decr=0
        cres=0
        if i==0:
            if a[i]<a[i+1]:
                cres=cres+1
            else:
                break
        else:
            if a[i]<a[i+1]:
                cres=cres+1
                if a[i]>[a+1]:
                    decr=decr+1
            else:
                decr=decr+1
            
    if cres>1 and decr>1:
        return(True)
    else:
        return(False)
    
    


n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(0,n,1):
    d=int(input('Digite o valor:'))
    a.append(d)
    
if pico(a):
    print('S')
else:
    print('N')