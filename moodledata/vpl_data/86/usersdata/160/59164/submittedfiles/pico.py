# -*- coding: utf-8 -*-

def pmax(a):
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            return(i)

def pico(n):
    #CONTINUE...
    cont=0
    x=pmax(a)
    for i in range(x,len(a)-1,1):
        if a[i]>a[i+1]:
                cont=cont+1
    if cont==(len(a)-x)-1:
        return True
    else:
        return False

b=[]
n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
for i in range(1,n+1,1):
    valor=int(input('Digite o elementos da lista:'))
    b.append(valor)
    
if pico(b):
    print('S')
    
else:
    print('N')
    

    