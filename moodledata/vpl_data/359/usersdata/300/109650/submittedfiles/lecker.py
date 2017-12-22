# -*- coding: utf-8 -*-
n = int(input('Digite o número de elementos nas listas: '))
a = []
b = []
for i in range(0,n,1):
    a.append(int(input('Digite um elemento de a: ')))
for i in range(0,n,1):
    b.append(int(input('Digite um elemento de b: ')))

def lecker(a):
    t = 0
    
    if a[0] > a [1] and a[n-2] >= a [n-1]:
        cont = 0
        for i in range(1,n,1):
            if a[i-1] >= a[i]:
                cont = cont + 1
        if cont == (n-1):
            t = t + 1
            
    if a[0] <= a[1] and a[n-2] < a[n-1]:
        cont = 0
        for i in range(1,n,1):
            if a[i] >= a[i-1]:
                cont = cont + 1
            if cont == (n-1):
                t = t + 5
                
    if a[0] < a[1] and a[n-2] > a[n-1]:
        for i in range(0,n-1,1):
            h = 0
            p = 0
            if a[i] < a[i+1]:
                continue
            else:
                p = i
                break
        for j in range(p,n-1,1):
            if a[j] > a[j+1]:
                continue
            else:
                h = 1
                break
        if h == 1:
            return False
        else:
            return True
            
    if t == 1:
        return True
    elif t == 5:
        return True
    else:
        return False
        
            
if lecker(a):
    print ('S')
else:
    print ('N')
if lecker(b):
    print ('S')
else:
    print ('N')    
    
        
    

