# -*- coding: utf-8 -*-
def pico(lista,n,p,v):
    p = 0
    v = 0
    for i in range(1,n-1,1):
        if lista[i-1] < lista[i] and lista[i] > lista[i+1]:
            p = p+1
        elif lista[i-1] > a[i] and lista[i] < lista[i+1]:
            v = v+1
            break
    if p == 1 and v ==0:
        return True
    else:
        return False
    
    
n = int(input('Digite a quantidade de elementos da lista: '))
a = []

for i in range(0,n,1):
    a.append(int(input('Digite a%d: ' %(i+1))))
if pico(a,n,0,0):
    print('S')
else:
    print('N')




'''
n = int(input('Digite a quantidade de elementos da lista: '))
a = []
for i in range(0,n,1):
    a.append(int(input('Digite a%d: ' %(i+1))))
print(a)
if len(a) <= 3:
    for i in range(0,3,1):
        if i < 2 and i !=0:
            if a[i-1] > a[i]:
                print('N')
                break
        if i == 2:
            if a[i-1] > a[i]:
                print('S')
                break
if len(a) >3:
    for i in range(0,n,1):
        if i == 2:
            if a[i-1] > a[i]:
                print('N')
            else:
                print('S')

'''
    

                
        
        
    
    
    
    
    
    
    
    
    
    