# -*- coding: utf-8 -*-
while True:
    n=int(input('Digite um numero:'))
    if n>=1:
        break

soma=0

while n>=1 :
    re=n%10
    n=n//10
    soma+=re
    
print(soma)
    


    

