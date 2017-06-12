# -*- coding: utf-8 -*-

def pico(a):
    for i in range(0,len(a),1):
        while a[i]<a[i+1]:
            cont=cont+1
    return(cont)

    
    


n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range(0,n,1):
    p=int(input('digite um valor'))
    a.append(p)
if pico(a):
    print('S')
else:
    print('N')
print(pico(a))
