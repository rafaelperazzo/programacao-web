# -*- coding: utf-8 -*-
n=int(input('Digite um número:'))
if n<9999999:
    print('NAO SEI')
elif n>99999999:
    print('NAO SEI')
else:
    print('8')
resto= n % 10000000    
soma=(soma+resto)/n
print(soma)
    

    
    

