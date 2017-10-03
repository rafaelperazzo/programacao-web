# -*- coding: utf-8 -*-
n=int(input('Digite um número:'))
if n<9999999:
    print('NAO SEI')
elif n>99999999:
    print('NAO SEI')
else:
    d1=n//(10**7)
    d2=(n-(d1*(10**7)))//(10**6)
    d3=(n-((d1*(10**7)+d2*(10**6))))//(10**5)
    d4=(n-((d1*(10**7)+d2*(10**6)+d3*(10**5))))//(10**4)
soma=d1+d2+d3+d4
    
    

