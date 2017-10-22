# -*- coding: utf-8 -*-
p=int(input('Digite o valor do maior numero: '))
q=int(input('Digite o valor do menor numero: '))

expoente=1
while q//10>0:
    expoente=expoente+1
    q=q//10
    if p%10**expoente==q:
        print('S')
        p//10
    else:
        print('N')
    

   
    
    
        
    
    

        


