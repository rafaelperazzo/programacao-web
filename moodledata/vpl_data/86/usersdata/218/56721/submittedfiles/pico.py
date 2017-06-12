# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    cont=0
    for i in range (1,len(lista)+1,1):
        if a[1]>a[0]:
            if a[i+1]<a[i]:
                cont=1
    if cont==0:
        return True
    else:
        return False
    


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
for i in range (0,n,1):
    num=int(input('digite o numero:'))
    a.append(num)
    
if pico(a):
    print('S')
else:
    print('N')