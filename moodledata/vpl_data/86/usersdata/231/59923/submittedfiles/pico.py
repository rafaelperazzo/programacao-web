# -*- coding: utf-8 -*-

def picomax(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            return i
def pico(c):
    f=picomax
    for i in range(0,len(c)-1,1):
        if c[i]<c[i+1]:
            return False
    return True
    
        
    return (cont)


n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(0,n,1):
    b=int(input('b:'))
    a.append(b)
        
if pico(a):
    print('S')
else:
    print('N')

#CONTINUE...
