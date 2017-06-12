# -*- coding: utf-8 -*-
def primo(n):
    cont=0
    for i in range(5,n,1):
        if n%i==0:
            cont=cont+1
        else:
            cont=cont+1
    if cont==0:
        return(True)
    else:
        return(False)
a=int(input('digite a :'))
if primo(a):
    print('primo')
    print(primo(a))
else:
    print('não primo')



    
   
        
    
