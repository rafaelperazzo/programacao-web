# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    cont=0
    if a[0]<a[1]:
        for i in range (0,len(lista),1):
            if cont==0:
                if a[i]<a[i-1]:
                    cont=1
            elif cont==1:
                if a[i]>a[i-1]:
                    cont=2
            else:
                return False
        return True
        
n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
a=[]
for i in range (0,n,1):
    num=int(input('digite o numero:'))
    a.append(num)
    
if pico(a):
    print('S')
else:
    print('N')