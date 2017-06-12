# -*- coding: utf-8 -*-
def primo(a):
    cont=0
    for i in range(1,a+1,1):
        if a%i==0:
            cont=cont+1
            break
    if cont==2:
        return True  
    else:
        return False 
p=int(input('digite o número:'))
q=int(input('digite o número:'))
if primo(p)==True and primo(q)==True:
    if b==a+2:
        print('S')
elif  primo(p)==False or primo(q)==False:
    print('N')

        

            









if b==a+2:
    print('S')
else:
    print('N')