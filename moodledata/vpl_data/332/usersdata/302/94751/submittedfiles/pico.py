# -*- coding: utf-8 -*-

#def pico(lista):

    #CONTINUE...
    


n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
a = []
for i in range(0,n,1):
    a.append(int(input('Digite a%d: ' %(i+1))))
print(a)
# Se tiver Dígitos consecutivos iguais, não é um pico
for i in range(0,n,1):
    if i < n and i !=0:
        if a[i-1] == a[i]:
            print('N')
            break
#se não decrescer até o final, tbm não é pico
for i in range(0,n,1):
    if i > 2:
        if a[i-1] < a[i]:
            print('N')
#se a[0] > a[1], não é um pico
if a[0] > a[1]:
    print('N')
#se a for crescente e não decrescer, não é um pico
    if a == sorted(a):
        print('N')
        if a[0] < a[1] and a[1] > a[2]:
            print('S')
    

                
        
        
    
    
    
    
    
    
    
    
    
    