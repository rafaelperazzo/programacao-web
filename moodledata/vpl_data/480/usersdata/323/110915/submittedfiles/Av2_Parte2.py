# -*- coding: utf-8 -*-
while True:
    n=int(input('Digite um valor: '))
    if n>=1:
        break


    
resto1=n%10
resto2=(n-n%10)%10
resto3=(n-((n-n%10)%10))%10

resto4=(n-((n-((n-n%10)%10))%10))%10
resto5=(n-(n-((n-((n-n%10)%10))%10))%10)%10

soma=resto1+resto2+resto3+resto4+resto5
print(soma)
    
    
