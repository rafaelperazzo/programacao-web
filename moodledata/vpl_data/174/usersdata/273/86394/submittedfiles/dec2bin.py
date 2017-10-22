# -*- coding: utf-8 -*-
p=int(input('Digite o valor do maior inteiro: '))
q=int(input('Digite o valor do menor inteiro: '))

expoente=0
while (q%10)>0:
    expoente=expoente+1
    if (p%10**expoente)==q:
        print ('S')
    else:
        print('N')
    p==p//10
    q==q//10
    break
    
        
    
    

        


