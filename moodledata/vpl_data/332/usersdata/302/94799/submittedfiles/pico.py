# -*- coding: utf-8 -*-

#def pico(lista):

    #CONTINUE...
n = int(input('Digite a quantidade de elementos da lista: '))
a = []
for i in range(0,n,1):
    a.append(int(input('Digite a%d: ' %(i+1))))
if a[0] < a[1]:
    pico = True
    subida = False
else: 
    pico = False
a[0] = a[1]
i = 2
while(i < n-1):
    if a[i-1] < a[i]:
        if not subida:
            pico == False
    else:
        pico == False
    a[i-1] = a[i]
    a[i] = a[i+1]
if subida:
    pico = False
if pico:
    print('S')
else:
    print('N')

'''
n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
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

    

                
        
        
    
    
    
    
    
    
    
    
    
    