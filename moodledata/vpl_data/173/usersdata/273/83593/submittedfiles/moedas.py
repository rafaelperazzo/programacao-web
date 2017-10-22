# -*- coding: utf-8 -*-
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de c: '))
qa=0
x9=0

while(qa<c):
    y= (a*qa)
    x= (c-y)
    if(x%b)==0:
        print(qa)
        print(x/b)
        break
    else:
        x9=x9+1
        qa=qa+1
if(x9==c):
    print('n')


    
    
    
    

    
    
    
    

