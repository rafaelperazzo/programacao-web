# -*- coding: utf-8 -*-
def primo(x):
    cont=0
    for i in range(1,x+1,1):
        if x%i==0:
            cont=cont+1
            break
    if cont==2:
        return True  
    else:
        return False 
a=int(input('digite o número:'))
b=int(input('digite o número:'))
if primo(p)==True and primo(q)==True:
    if b==a+2:
        print('S')


        

            









