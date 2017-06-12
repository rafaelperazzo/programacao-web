# -*- coding: utf-8 -*-
def primo(a):
    cont=0
    for i in range(1,a+1,1):
        if a%1==0:
            cont=cont+1
    if cont==2:
        return True  
    else:
        return False 
a=int(input('digite o número:'))
b=int(input('digite o número:'))
if primo(a):
    if primo(b):
        if b==a+2:
            print('S')
        else:
            print('N')
    

        

            









if b==a+2:
    print('S')
else:
    print('N')