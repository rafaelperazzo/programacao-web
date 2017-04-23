# -*- coding: utf-8 -*-
n=int(input('n:'))
produto=1
numerador=2
denominador=1
for i in range(1,n+1,1):
    produto=produto*(numerador/denominador)
    if i%2==1:
        denominador=denominador+2
    else:
        numerador=numerador+2
produto=produto*2
print('%.5f' %produto)
    
    
        
    
        
    

   


