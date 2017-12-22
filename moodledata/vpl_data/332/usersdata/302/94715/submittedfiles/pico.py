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
    if i < n:
        if a[i-1] == a[i]:
            print('N')
            break

            
                
        
        
    
    
    
    
    
    
    
    
    
    